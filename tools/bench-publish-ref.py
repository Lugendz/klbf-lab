# Publishes one of our own reference runs (KLBF Lab test machine) with its card kept in the repository.
# Usage: python -I tools/bench-publish-ref.py <KLBF-Bench-BM-v1-...json> <card.png>
# Copies the JSON to docs/klbf/bench/bm-v1/ and the PNG to docs/klbf/bench/bm-v1/cards/<serial>.png,
# adds or updates its submissions.json entry (login PastiiJay, reference), checks the result with
# tools/bench-check.py --login PastiiJay, then regenerates the board and the README with bench-board.py.
# Nothing is copied when the check fails. Commit and push are left to you.
import json, shutil, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FOLDER = HERE.parent / 'docs' / 'klbf' / 'bench' / 'bm-v1'


def run(*args):
    if subprocess.run([sys.executable, '-I', *map(str, args)]).returncode:
        sys.exit(f'{Path(args[0]).name} failed: nothing more done')


def main():
    if len(sys.argv) != 3:
        sys.exit('usage: bench-publish-ref.py <result.json> <card.png>')
    src, png = map(Path, sys.argv[1:])
    if png.suffix.lower() != '.png' or png.read_bytes()[:8] != b'\x89PNG\r\n\x1a\n':
        sys.exit(f'{png}: not a PNG')
    run(HERE / 'bench-check.py', src, '--login', 'PastiiJay')
    s = json.loads(src.read_text(encoding='utf-8-sig'))['serial']
    shutil.copyfile(src, FOLDER / src.name)
    (FOLDER / 'cards').mkdir(exist_ok=True)
    shutil.copyfile(png, FOLDER / 'cards' / f'{s}.png')
    subs_path = FOLDER / 'submissions.json'
    subs = json.loads(subs_path.read_text(encoding='utf-8-sig')) if subs_path.exists() else {}
    subs[s] = {**subs.get(s, {}), 'login': 'PastiiJay', 'card': f'bench/bm-v1/cards/{s}.png',
               'repo': 'https://github.com/PastiiJay/klbf-lab', 'reference': True}
    subs_path.write_text(json.dumps(subs, indent=2, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')
    run(HERE / 'bench-board.py')
    print(f'Reference run {s} ready: review git diff, then commit and push.')


if __name__ == '__main__':
    main()
