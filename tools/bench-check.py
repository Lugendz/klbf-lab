# Checks one KLBF Lab Bench BM-v1 result file and prints its row for docs/klbf/BAYSIDE-MORNING-V1.md.
# Usage: python -I tools/bench-check.py KLBF-Bench-BM-v1-<serial>.json [--login <GitHub login>] [--card <URL>]
# Exit 0 and one table row when the result is acceptable; exit 1 and the problems otherwise.
# Mirrors the game side (crates/victory-gpu/src/klbf_bench.rs): same fields, same verdict rules.
# Serial (schema 1): the first 8 hex of SHA-256 over the canonical JSON without the serial and share
# fields (the share line carries the serial): keys sorted, separators (',', ':'), UTF-8 (non-ASCII
# kept), floats rounded to 2 decimals. Min and max fps are the slowest and fastest 1-second windows,
# listed in fps_per_second; the 1 % and 5 % lows are per frame.
# --login: the submitter; the player on the card must be that login or "anonymous".
# --card: the card PNG attached to the submission issue.
import argparse, hashlib, json, math, re, sys
from pathlib import Path

TARGET_S = 300
# 27/11: -BenchLength runs: 5 (BM-v1), 15 (Medium), 30 (Long) or 60 (Marathon) minutes.
TARGETS = {300: '', 900: '-Medium', 1800: '-Long', 3600: '-Marathon'}
FIELDS = {
    'schema': int, 'bench': str, 'test': str, 'test_id': str, 'stamp': str, 'reason': str, 'stop': str, 'serial': str,
    'date': str, 'project': str, 'project_source': str, 'sha': str, 'player': str, 'gpu': str,
    'gpu_vram_gb': (int, float), 'cpu': str, 'ram_gb': (int, float), 'os': str, 'duration_s': (int, float),
    'target_s': int, 'frames': int, 'fps': dict, 'fps_per_second': list, 'pct_time_ge_12fps': (int, float),
    'freezes_over_200ms': int, 'longest_frame_ms': (int, float), 'black_frames': int,
    'device_removed': bool, 'inputs_blocked': int, 'share': str,
}
FPS = ('avg', 'median', 'low_1pct', 'low_5pct', 'min', 'max')
# Quality settings under "settings" (each optional; shown in the Settings column when present).
SETTINGS = (('profile', 'profile {}'), ('upscaler', '{}'), ('texture_max_dim', 'textures ≤ {} px'),
            ('pipelines_skipped', '{} pipelines skipped'), ('pipelines_denied', '{} pipelines denied'),
            ('draws_per_frame', '{} draws/frame'), ('dropped_draws_pct', '{} % draws dropped'))
CARD = 'https://github.com/user-attachments/'
LOGIN = re.compile(r'^[A-Za-z0-9](?:[A-Za-z0-9]|-(?=[A-Za-z0-9])){0,38}$')
R2 = 0.005  # half a unit of the 2 decimals the game writes


def serial(d):
    canon = json.dumps({k: v for k, v in d.items() if k not in ('serial', 'share')}, sort_keys=True, separators=(',', ':'),
                       ensure_ascii=False)
    return hashlib.sha256(canon.encode('utf-8')).hexdigest()[:8]


def check(d, name=None, login=None):
    """Every problem with one parsed result; empty when it is acceptable."""
    if not isinstance(d, dict):
        return ['not a JSON object']
    p = [f'{k}: missing or wrong type' for k, t in FIELDS.items()
         if not isinstance(d.get(k), t) or (t is int and isinstance(d.get(k), bool))]
    fps = d.get('fps') if isinstance(d.get('fps'), dict) else {}
    p += [f'fps.{k}: missing or not a number' for k in FPS
          if not isinstance(fps.get(k), (int, float)) or isinstance(fps.get(k), bool) or not math.isfinite(fps[k])]
    per_s = d.get('fps_per_second') if isinstance(d.get('fps_per_second'), list) else []
    if any(not isinstance(x, (int, float)) or isinstance(x, bool) or not math.isfinite(x) or x <= 0 for x in per_s):
        p.append('fps_per_second: not all positive numbers')
    if 'settings' in d and not isinstance(d['settings'], dict):
        p.append('settings: not an object')
    if p:
        return p
    if (d['schema'], d['bench'], d['test']) != (1, 'KLBF Lab Bench', 'Bayside Morning v1') or d['test_id'] != 'BM-v1' + TARGETS.get(d['target_s'], '?'):
        p.append('not a BM-v1 result')
    # Duration: the full 5:00 from the first world frame.
    target = d['target_s'] if d['target_s'] in TARGETS else TARGET_S
    if d['target_s'] not in TARGETS or d['duration_s'] < target or d['stop'] not in ('5:00 reached', 'the full time reached'):
        p.append(f"duration {d['duration_s']} s / stop '{d['stop']}': the {target // 60}:00 run did not complete")
    # Verdict, re-derived with the game's rules.
    n, longest = d['frames'], d['longest_frame_ms']
    if d['stamp'] != 'CERTIFIED':
        p.append(f"stamp {d['stamp']}: only CERTIFIED results are listed")
    if d['device_removed']:
        p.append('device removed')
    if n < 300:
        p.append('fewer than 300 frames')
    if d['black_frames'] * 100 > n:
        p.append('black frames over 1 %')
    if longest >= 10_000:
        p.append('a stall of 10 s or more')
    # Figures against each other.
    a = fps
    if a['avg'] <= R2 or longest <= 0:
        return p + ['no frame rate']
    total_hi, total_lo = n / (a['avg'] - R2), n / (a['avg'] + R2)  # seconds of frames
    if total_hi < target - 0.1 or total_lo > target + longest / 1000 + 0.1:
        p.append(f"frames / avg fps = {n / a['avg']:.1f} s, not the {target // 60}:00 measured")
    # Min and max: the slowest and fastest 1-second windows (the average when there is none).
    lo, hi = (min(per_s), max(per_s)) if per_s else (a['avg'], a['avg'])
    if abs(a['min'] - lo) > 2 * R2 or abs(a['max'] - hi) > 2 * R2:
        p.append('min / max fps do not match the per-second figures')
    if not a['low_1pct'] <= a['low_5pct'] + 2 * R2 <= a['avg'] + 4 * R2:
        p.append('fps figures out of order (1 % low ≤ 5 % low ≤ avg)')
    pct = d['pct_time_ge_12fps']
    if not 0 <= pct <= 100 or (longest < 1000 / 12 - 0.05 and pct < 100 - 2 * R2):
        p.append('time ≥ 12 fps does not match the frame times')
    fz = d['freezes_over_200ms']
    if not 0 <= fz <= n or (fz > 0 and longest <= 200 - 0.05) or (fz == 0 and longest > 200 + 0.05):
        p.append('freeze count does not match the longest frame')
    # Serial: the content hash, the same in the file name and the share line.
    s = d['serial']
    if s != serial(d):
        p.append(f'serial {s} does not match the content (expected {serial(d)}): the file was changed')
    if name is not None and not re.fullmatch(rf'KLBF-Bench-BM-v1(?:-Medium|-Long|-Marathon)?-(?:\d{{8}}-\d{{4}}-)?{re.escape(s)}\.json', Path(name).name):
        p.append(f'file name does not match serial {s}')
    if not d['share'].endswith(f"| {d['stamp']} | {s}") or f"{d['project']}@{d['sha']}" not in d['share']:
        p.append('share line does not match the result')
    if login is not None and d['player'] != 'anonymous' and d['player'].lower() != login.lower():
        p.append(f"player '{d['player']}' is not the submitter's GitHub login ({login}) or 'anonymous'")
    return p


def cell(v):
    return str(v).replace('|', '\\|').replace('\n', ' ').strip()


def settings(d):
    st = d.get('settings') or {}
    return ' · '.join(f.format(cell(st[k])) for k, f in SETTINGS if st.get(k) not in (None, ''))


REFERENCE = 'reference run — KLBF Lab test machine'


def player_link(d, reference=False):
    """Linked only once check() has matched the player to the submitter's login."""
    player = cell(d['player'])
    if player != 'anonymous' and LOGIN.match(player):
        player = f'[{player}](https://github.com/{player})'
    return f'{player} ({REFERENCE})' if reference else player


def project_link(d, repo=None):
    """A build from git links its commit; otherwise the repo URL given with the submission."""
    proj, sha = cell(d['project']), cell(d['sha'])
    if d['project_source'] == 'git':
        return f'[{proj}@{sha}](https://github.com/{proj}/tree/{sha})'
    return f'[{proj}@{sha}]({repo})' if repo else f'{proj}@{sha}'


def row(d, stem, card=None, repo=None, reference=False):
    """The board row; stem is the result's path without extension, relative to the board page."""
    proof = f'[JSON]({stem}.json)' + (f' · [card]({card})' if card else '')
    a = d['fps']
    return ' | '.join([
        '', player_link(d, reference), project_link(d, repo), f"{cell(d['gpu'])} {d['gpu_vram_gb']:.0f} GB", cell(d['cpu']), f"{d['ram_gb']:.0f} GB",
        f"{a['avg']:.1f}", f"{a['median']:.1f}", f"{a['low_1pct']:.1f}", f"{d['pct_time_ge_12fps']:.1f}",
        settings(d), cell(d['date'])[:10], proof, '']).strip()


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
    ap = argparse.ArgumentParser()
    ap.add_argument('json'); ap.add_argument('--login'); ap.add_argument('--card')
    a = ap.parse_args()
    if a.card and not a.card.startswith(CARD):
        sys.exit(f'--card must be an image attached on GitHub ({CARD}...)')
    path = Path(a.json)
    try:
        d = json.loads(path.read_text(encoding='utf-8-sig'))
    except (OSError, ValueError) as e:
        sys.exit(f'{path}: {e}')
    problems = check(d, path.name, a.login)
    if problems:
        print('\n'.join(f'{path.name}: {x}' for x in problems), file=sys.stderr)
        sys.exit(1)
    print(row(d, f'bench/bm-v1/{path.stem}', a.card))


if __name__ == '__main__':
    main()
