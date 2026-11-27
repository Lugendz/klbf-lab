# KLBF Lab Bench · Bayside Morning v1 (BM-v1)

The goal is cooperation: one repeatable test so each project can check its own builds, compare notes, and follow the changes that really work.

One 5-minute run, always the same scene, to compare machines and versions. The build measures
itself: you load one save, press Continue and touch nothing. Results: [Bayside Morning v1 — Results](BAYSIDE-MORNING-V1.md).

## Prerequisites

- A KLBF Lab build that includes the bench, and your own legally obtained copy of the title.
- The title already reaches gameplay on your machine.
- A progress point at the male lead's house (about 3 % progress, where you can first save in his bed).
- Nothing else heavy running during the 5 minutes.

### A build without the bench (fallback)

Another project can add the bench to its own build: see
[ADD-THE-BENCH.md](https://github.com/PastiiJay/klbf-lab/blob/beta-2/docs/klbf/ADD-THE-BENCH.md).
Until then, or for a layer it does not fit, the same run can be measured from the build's log:
play the same save the same way, keep the console log, then:

```powershell
python -I tools/fps-session.py <log file> --bench bm-v1 --gpu "<GPU>" --cpu "<CPU>" --build "<owner/repo@commit>"
```

It keeps exactly 300 s of world time from the first world sample (a sample with the world on
screen) and prints the usual summary and share line, marked **NOT CERTIFIED (no input lock, no
card)**: nothing stops a press from changing the run, and there is no card or serial. Such a result
is fine for checking your own builds; the board lists only CERTIFIED runs.

## Make the save (once)

1. Sleep until the morning at the male lead's house.
2. Go down to the laundry room (the one with the washing machine), pick up the fishing book on the
   workbench and keep it in hand.
3. Press Start, then save in **slot 1**.
4. Each run: **Continue**, then don't touch anything.

Every run starts from this save, so the time of day, the light and the scene are the same for
everyone. Keep a copy of it as described in [MEASUREMENT.md](MEASUREMENT.md#keep-your-morning-save),
and keep your save files to yourself: they can carry your console profile's ids.

## Run

1. Set the variables (only the first is required):
   - `KLBF_BENCH=bm-v1` turns the bench on. Without it nothing changes.
   - `KLBF_BENCH_PLAYER=<GitHub login>` is written on the card (otherwise "anonymous"). The board
     only lists a run whose player is the submitter's GitHub login or "anonymous".
   - `VICTORY_SKIP_MOVIES=end` skips the intro movies.
2. Press **Continue** and check the first scene. The male lead should be in the laundry room with the
   fishing book in hand. If he is in front of the TV, Continue picked a different save. End that
   run and restart the bench. From the menu, choose **Load** and pick slot 1 below the autosave.
3. Touch nothing.

```powershell
$env:KLBF_BENCH = "bm-v1"; $env:KLBF_BENCH_PLAYER = "<GitHub login>"; $env:VICTORY_SKIP_MOVIES = "end"
```

The measurement starts at the first world frame. 5 seconds later input is blocked: the game gets an
idle controller and no keyboard; presses are only counted. Nothing is drawn over the game during the
run; only the time of each frame is recorded. At **5:00** the run stops by itself. **F10** or closing
the window stops early (PARTIAL, not comparable).

The card then covers the screen. A key or button closes it (or it closes after 60 s) and the game
exits.

## What the card means

- **Left**: the date and how the run ended ("5:00 complete · no input", or "PARTIAL m:ss / 5:00 – not comparable").
- **Round stamp**: the serial (8 characters, a SHA-256 fingerprint of the result file) and
  the date. The band across it is the verdict:
  - **CERTIFIED**: the full 5:00, the graphics device kept, at most 1 % black frames, no stall of 10 s
    or more, at least 300 frames.
  - **PARTIAL**: stopped before 5:00. Not comparable.
  - **INVALID**: 5:00 done, but one of the checks failed.
- **from:** the project and version (`owner/repo @ commit`), read from git at build time; "(declared)"
  when given by `KLBF_PROJECT_NAME`, "unknown (local build)" otherwise. Below it, the player.
- **Big number**: average fps.
- **Four boxes**: median fps; 1 % low (average of the slowest 1 % of frames); max fps (the fastest 1-second window); time ≥ 12 fps
  (share of the time spent at 12 fps or more).
- **Thin line**: freezes (frames over 200 ms), measured duration, inputs blocked.
- **Bold line**: the machine (GPU and its memory, CPU, RAM, Windows).
- **Share line**: the one-line summary.

## Your data stays on your PC

- The bench sends nothing anywhere: no network, no account, no upload.
- The card and the result files are written only to your own disk.
- The code is open: see `crates/victory-gpu/src/klbf_bench.rs`.
- Posting the card, or submitting a result to the board, is entirely your choice.
- The result files hold your frame figures (the average of each second and the summary figures, not
  each frame), the date and time of the run and its verdict, your hardware names (GPU and its memory,
  CPU, RAM, Windows version), the build's project and commit, the settings, and the nickname you
  chose. They also hold a few run checks: black frames, inputs blocked, shaders and pipelines
  compiled during the run, and the video and system memory in use at the end. No user name, no
  paths, no IDs.

## Where is my card?

- In the folder `bench-results` next to `victory.exe` (or in `KLBF_BENCH_DIR` if you set it).
- One file per run, named `KLBF-Bench-BM-v1-YYYYMMDD-HHMM-<serial>.png`, with matching `.json` and
  `.txt`. A new run never overwrites an older one.
- The full path is also printed in the console at the end of the run.
- To share: drag the PNG into Fluxer or a GitHub comment and paste the share line from the `.txt`.

## Share

Your results stay on your machine unless you choose to share or submit them.

- **To share**: post the card PNG with the share line from the `.txt` under it, on Fluxer or in a
  GitHub comment. For example:
  `[KLBF Lab Bench BM-v1] owner/repo@abc1234 | RX 9070 XT | Ryzen 7 9800X3D | avg 14.2 fps, 1% low 2.2 | CERTIFIED | 8e45f78d`
- **To appear on the board**: submit the JSON and attach the card PNG through the
  [result form](https://github.com/PastiiJay/klbf-lab/issues/new?template=bench-bm-v1.yml). Only
  CERTIFIED results are listed. Each one is checked with `python -I tools/bench-check.py <file>.json`.

Only the card, please: no screenshots of the game. When a shared result looks doubtful, we may ask
for its JSON.
