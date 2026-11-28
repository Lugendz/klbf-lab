# Bayside Morning v1 — Results

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
player is the submitter's GitHub login, or anonymous. Submit yours through the [result form](https://github.com/PastiiJay/klbf-lab/issues/new?template=bench-bm-v1.yml).
Within each group, rows are in order of GPU name, then date. Settings shows what the result file
records about quality.

## AMD

| Player | Project | GPU | CPU | RAM | avg | median | 1 % low | ≥ 12 fps % | Settings | date | proof |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [ZutphenAu](https://github.com/ZutphenAu) | [PastiiJay/klbf-lab@6f53d9a](https://github.com/PastiiJay/klbf-lab/tree/6f53d9a) | AMD Radeon RX 6950 XT 16 GB | 13th Gen Intel(R) Core(TM) i7-13700KF | 32 GB | 22.5 | 24.2 | 5.2 | 92.4 | profile X · FSR · 0 pipelines skipped · 0 pipelines denied · 3059.82 draws/frame · 0.0 % draws dropped | 2026-11-28 | [JSON](bench/bm-v1/KLBF-Bench-BM-v1-20261128-1620-863cb19e.json) · [card](https://github.com/user-attachments/assets/03cd35fe-d533-420a-b87e-b80efbe36fc1) |
| [PastiiJay](https://github.com/PastiiJay) (reference run — KLBF Lab test machine) | [PastiiJay/klbf-lab@a0687b7](https://github.com/PastiiJay/klbf-lab/tree/a0687b7) | AMD Radeon RX 9070 XT 16 GB | AMD Ryzen 7 9800X3D 8-Core Processor | 31 GB | 14.3 | 17.0 | 3.6 | 70.2 | profile S · FSR · textures ≤ 1024 px · 1 pipelines skipped · 0 pipelines denied · 8701.03 draws/frame · 0.0 % draws dropped | 2026-11-26 | [JSON](bench/bm-v1/KLBF-Bench-BM-v1-20261126-1653-5096b690.json) · [card](https://github.com/user-attachments/assets/c973f94d-651b-4feb-a90f-bdc82e23f5d0) |

## NVIDIA

| Player | Project | GPU | CPU | RAM | avg | median | 1 % low | ≥ 12 fps % | Settings | date | proof |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [vShotv](https://github.com/vShotv) | [PastiiJay/klbf-lab@bedecd6](https://github.com/PastiiJay/klbf-lab/tree/bedecd6) | NVIDIA GeForce RTX 4070 12 GB | AMD Ryzen 5 7600 6-Core Processor | 31 GB | 8.3 | 8.9 | 2.4 | 11.5 | profile X · none · textures ≤ 1024 px · 48 pipelines skipped · 0 pipelines denied · 6457.02 draws/frame · 0.65 % draws dropped | 2026-11-26 | [JSON](bench/bm-v1/KLBF-Bench-BM-v1-20261126-2011-eb51f9b4.json) · [card](https://github.com/user-attachments/assets/f3299aa6-89af-46b1-91a2-b7288f44b22f) |
