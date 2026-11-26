# Regenerates docs/klbf/BAYSIDE-MORNING-V1.md from every result in docs/klbf/bench/bm-v1/*.json.
# Usage: python -I tools/bench-board.py
# Every result must pass tools/bench-check.py; one that does not stops the run and nothing is written.
# docs/klbf/bench/bm-v1/submissions.json gives, per serial, the submitter's GitHub login and the card
# PNG attached to their issue: {"<serial>": {"login": "...", "card": "https://github.com/user-attachments/...",
# "repo": "https://...", "reference": true}} (repo: the form's project URL, used when the build has no
# git origin; reference: our own run on the KLBF Lab test machine). A reference run may instead keep its
# card in the repository: "card": "bench/bm-v1/cards/<serial>.png" (relative to docs/klbf/; see
# tools/bench-publish-ref.py). Community runs need the GitHub-attached card.
# Also rewrites the "Latest run" line of README.md, between <!-- latest-run-start --> and -end -->.
# The player on the card must be that login or "anonymous".
import importlib.util, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('bench_check', HERE / 'bench-check.py')
bc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bc)

ROOT = HERE.parent
DOCS = ROOT / 'docs' / 'klbf'
FORM = 'https://github.com/PastiiJay/klbf-lab/issues/new?template=bench-bm-v1.yml'
HEAD = f"""# Bayside Morning v1 — Results

Real measured examples, grouped by hardware, to help you find which project runs well on a PC like
yours. Every project listed gets a link.

The goal is cooperation: one repeatable test so each project can check its own builds, compare notes, and follow the changes that really work.

> **Indicative only.** These are self-measured runs: we check each result file (duration, no input,
> consistency, fingerprint), but we have not seen each player's screen, so we cannot confirm every
> effect was drawn correctly. A higher fps can come from lower settings or skipped shaders.
> Thank you to everyone who contributed a run.

Each run is the same 5-minute scene, measured by the build itself from the first world frame, with
input blocked after 5 s ([procedure](BENCH-BM-V1.md)). Only CERTIFIED results are listed. Each one
is checked with `tools/bench-check.py`: test and version, the full 5:00, the verdict, the frame
figures against each other, and the serial (a SHA-256 fingerprint of the file's content). The
player is the submitter's GitHub login, or anonymous. Submit yours through the [result form]({FORM}).
Within each group, rows are in order of GPU name, then date. Settings shows what the result file
records about quality.
"""
TABLE = """| Player | Project | GPU | CPU | RAM | avg | median | 1 % low | ≥ 12 fps % | Settings | date | proof |
|---|---|---|---|---|---|---|---|---|---|---|---|
"""
VENDORS = (('AMD', ('amd', 'radeon')), ('NVIDIA', ('nvidia', 'geforce', 'rtx', 'gtx', 'quadro')),
           ('Intel', ('intel', ' arc ')))


def latest_line(d, stem, card, repo, reference):
    """The README's one line for the most recent run; stem relative to the repository root."""
    a, st = d['fps'], d.get('settings') or {}
    short = ', '.join(bc.cell(st[k]) for k in ('profile', 'upscaler') if st.get(k) not in (None, ''))
    line = ' · '.join(x for x in [
        f"> **Latest run:** {bc.cell(d['date'])[:10]}", bc.player_link(d), bc.project_link(d, repo),
        f"{bc.cell(d['gpu'])} / {bc.cell(d['cpu'])}",
        f"{a['avg']:.1f} fps avg (median {a['median']:.1f}, 1 % low {a['low_1pct']:.1f})",
        f'profile {short}' if st.get('profile') else short, f'[card]({card}) · [JSON]({stem}.json)',
        bc.REFERENCE if reference else ''] if x)
    # The card itself (our own drawing and the run's figures, no game picture), shown under the line.
    return line + (f'\n>\n> <a href="{card}"><img src="{card}" width="560" alt="KLBF Lab Bench card"></a>' if card else '')


def vendor(gpu):
    g = f' {gpu.lower()} '
    return next((v for v, words in VENDORS if any(w in g for w in words)), 'Other')


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
    folder = DOCS / 'bench' / 'bm-v1'
    subs = folder / 'submissions.json'
    subs = json.loads(subs.read_text(encoding='utf-8-sig')) if subs.exists() else {}
    rows, bad = [], []
    for path in sorted(folder.glob('KLBF-Bench-BM-v1-*.json')):
        try:
            d = json.loads(path.read_text(encoding='utf-8-sig'))
        except ValueError as e:
            bad.append(f'{path.name}: {e}')
            continue
        sub = subs.get(d.get('serial') if isinstance(d, dict) else None)
        card = str(sub.get('card', '')) if isinstance(sub, dict) else ''
        # Only our own reference runs may keep the card in the repository (cards/<serial>.png).
        in_repo = isinstance(sub, dict) and sub.get('reference') is True \
            and card == f"bench/bm-v1/cards/{d.get('serial')}.png" and (DOCS / card).is_file()
        if not isinstance(sub, dict) or not isinstance(sub.get('login'), str) \
                or not (card.startswith(bc.CARD) or in_repo):
            bad.append(f'{path.name}: no submissions.json entry with a login and a GitHub-attached card'
                       ' (or, for a reference run, its card at docs/klbf/bench/bm-v1/cards/<serial>.png)')
            continue
        problems = bc.check(d, path.name, sub['login'])
        # A card nickname that differs from the submitter's login is shown as the login (the real, linked account).
        if problems and all('is not the submitter' in x for x in problems):
            d['player'], problems = sub['login'], []
        bad += [f'{path.name}: {x}' for x in problems]
        if not problems:
            repo = sub['repo'] if str(sub.get('repo', '')).startswith('https://') else None
            ref = sub.get('reference') is True
            rows.append((vendor(d['gpu']), d['gpu'], d['date'], d['serial'],
                         latest_line(d, f'docs/klbf/bench/bm-v1/{path.stem}', 'docs/klbf/' + card if in_repo else card,
                                     repo, ref),
                         bc.row(d, f'bench/bm-v1/{path.stem}', card, repo, ref)))
    if bad:
        sys.exit('\n'.join(bad))
    groups = [v for v, _ in VENDORS] + ['Other']
    body = ''.join(f'\n## {v}\n\n' + TABLE + ''.join(r[-1] + '\n' for r in sorted(rows) if r[0] == v)
                   for v in groups if any(r[0] == v for r in rows)) or '\n_No results yet._\n'
    (DOCS / 'BAYSIDE-MORNING-V1.md').write_text(HEAD + body, encoding='utf-8', newline='\n')
    readme = ROOT / 'README.md'
    text = readme.read_text(encoding='utf-8')
    # The README shows OUR latest reference run (the KLBF Lab test machine), never a community run:
    # community results live in the board (Yvan, 26/11: the homepage must stay under our control).
    refs = [r for r in rows if bc.REFERENCE in r[4]]
    line = max(refs, key=lambda r: r[2])[4] if refs else '> _Latest run: none yet._'
    new, n = re.subn(r'(<!-- latest-run-start -->\n).*?(\n> ?<!-- latest-run-end -->)',
                     lambda m: m[1] + line + m[2], text, count=1, flags=re.S)
    if n != 1:
        sys.exit('README.md: the latest-run markers are missing')
    readme.write_text(new, encoding='utf-8', newline='\n')
    print(f'{len(rows)} result(s) written to docs/klbf/BAYSIDE-MORNING-V1.md and the README')


if __name__ == '__main__':
    main()
