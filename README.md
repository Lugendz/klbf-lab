<p align="center"><img src="docs/klbf/logo.svg" width="120" alt="KLBF Lab"></p>
<h1 align="center">KLBF Lab</h1>
<p align="center">
  <a href="https://github.com/PastiiJay/klbf-lab/releases/latest"><img src="https://img.shields.io/badge/stable-v26.11.4-1f46c8" alt="stable: v26.11.4"></a>
  <a href="#stable-v26114-28-nov-2026"><img src="https://img.shields.io/badge/BM--v1%20certified-30.2%20fps%20with%20frame%20generation%20(base%2016.0)-2ea44f" alt="BM-v1 certified: 30.2 fps with frame generation, base 16.0"></a>
  <a href="#stable-v26114-28-nov-2026"><img src="https://img.shields.io/badge/real%20play-45%20min%20without%20a%20crash-2ea44f" alt="45 minutes of play without a crash"></a>
  <img src="https://img.shields.io/badge/license-GPL--3.0-555" alt="GPL-3.0">
  <a href="docs/klbf/MEASUREMENT.md"><img src="https://img.shields.io/badge/fps-shared%20measurement%20method-2ea44f" alt="shared measurement method"></a>
</p>

Runs the Xbox Series build of the title on a Windows PC, from your own copy. **Best on AMD Radeon** (tested on an RX 9070 XT), works on other DirectX 12 cards.
**No game files here:** you need your own copy of the title.

## Stable: v26.11.4 (28 Nov 2026)

### [Download KLBF Lab v26.11.4 (KLBF-Lab.zip)](https://github.com/PastiiJay/klbf-lab/releases/latest/download/KLBF-Lab.zip)

- **Auto-update:** one click, your saves and settings kept.
- **Desktop shortcut,** like any game.
- **A settings window with every option:** Profile X / S, AMD FSR 4, FSR 3.1 or the built-in upscaler, presets, output size, frame generation (FG x2), screen choice, window or borderless fullscreen.
- **Shaders prepared once,** with a real progress bar.
- **Built-in benchmark** with certified cards you can share.
- **Built-in save manager:** slots, a backup before every launch, restore, copy over.
- **Keyboard and mouse** (Controls tab: on/off, sensitivity, invert, keys), next to a controller, with **controller rumble**.
- **In game:** F8 screenshots with your stats, F10 settings, F11 restart, Alt+Enter fullscreen.
- **Live stats in the title bar:** fps, base fps, 1 % low, upscaler, VRAM, RAM.
- **Privacy:** no paths, user or PC names shown unless you press Show.
- **Works on AMD RX 6000 / 7000 / 9000 and NVIDIA RTX 20 and newer** (FSR 3.1 outside RDNA 4).

**Start in 4 steps**

1. **Extract** the zip anywhere, then open the "KLBF Lab" folder.
2. **Double-click "KLBF Lab.cmd"** (Windows may hide the ".cmd" part). Later, use the desktop shortcut it can create.
3. **Choose your game folder** (your own copy).
4. **Play.**

The first start prepares the shaders (one progress bar, once) and downloads two official components, each file checked: Microsoft's DirectX 12 Agility SDK and AMD FSR (FidelityFX SDK v2.4.0). KLBF Lab is not signed: if Windows SmartScreen shows up, click "More info" then "Run anyway". [Release page](https://github.com/PastiiJay/klbf-lab/releases/latest) (SHA-256 of the zip) · source: branch [`stable-amd`](https://github.com/PastiiJay/klbf-lab/tree/stable-amd), tag `v26.11.4`. Already on v26.11.1 to v26.11.3? Click **Update** in the launcher.

**Measured on our PC** (RX 9070 XT, Ryzen 7 9800X3D, 32 GB):

<!-- latest-run-start -->
> **Latest run:** 2026-11-27 · **v26.11.1** · Profile X, FSR 4 Balanced 847p → 1440p, frame generation x2 · Radeon RX 9070 XT / Ryzen 7 9800X3D / 32 GB · **30.2 fps with frame generation (base 16.0)**, BM-v1 5:00 certified
> <!-- latest-run-end -->

- **45 min of play without a crash** on this version, in the open world.

**Requirements**

| | |
|---|---|
| Graphics card | AMD Radeon RDNA 2, 3 or 4 (RX 6000, 7000, 9000), NVIDIA GeForce RTX 20 series or newer |
| Video memory | 16 GB recommended |
| RAM | 32 GB recommended |

New in v26.11.4: keyboard and mouse, controller rumble, F8 overlay fixes, a fix for a crash at the start of the intro (#69, #116), the big Play button becomes Update when an update exists, and the bench form asks "Where were you?" and shows a Save ID. Earlier fixes: the launcher opens where antivirus or restricted Windows blocked its screen helper (v26.11.2) and starts from "KLBF Lab.cmd" (v26.11.3); RX 6000 device loss at world load (#127), an AMD compiler crash on RX 9070 XT, the high-performance GPU on laptops with two GPUs (#47). Everything, with every switch: **[CHANGELOG.md](https://github.com/PastiiJay/klbf-lab/blob/stable-amd/CHANGELOG.md)**.

## Benchmark

KLBF Lab Bench BM-v1: 5 minutes, hands-off, wherever you like in the game, with a certified card at the end. Say where you were on your post (city, countryside, indoors, night...). [How to run it](docs/klbf/BENCH-BM-V1.md) · [results by hardware](docs/klbf/BAYSIDE-MORNING-V1.md) · post yours with the [Bench result form](https://github.com/PastiiJay/klbf-lab/issues/new?template=bench-bm-v1.yml).

Issues and test reports: [this repository's issues](https://github.com/PastiiJay/klbf-lab/issues).

## What we want to improve

Everything we have seen and want to make better, from your reports and our own play. **No particular order**, and no dates: each item ships when it works.

- **Crashes** at launch and in the first minutes on some PCs.
- **Brightness** issues in some scenes.
- **Graphics issues** on some objects: flickering, missing parts, colours.
- **Shadows.**
- **Sound:** some effects are still silent.
- **Keyboard and mouse.**
- **Controller vibration.**
- **Frame generation** on more cards.
- **Lower RAM use.**
- **Ultrawide screens.**
- **Launcher and bench** improvements.
- **NVIDIA** support.

Seen something else? [Open an issue](https://github.com/PastiiJay/klbf-lab/issues).

## Credits

**v26.11.4:**
- **Domi**, **pacoravan**, **Dominic**, **MalarkZA** and **Aphantasiac**: the reports behind this build.
- **LooperSalty** (AnyXboxX) and **eikkapine**: the ideas behind keyboard and mouse.

**v26.11.1 to v26.11.3:**
- **INGLIP**, **deydey103** and **Solar**: the launcher error reports behind v26.11.2.
- **Op-lite's victory-scarlett** (no longer public): the base this version is built on.
- **cool_fox**: ambient light estimate; **Ryuki**: foliage fix.
- **[eikkapine](https://github.com/eikkapine)** (victory-amd): the ideas behind the experimental switches.
- **MalarkZA**, **[kyokyotosh](https://github.com/kyokyotosh)** and **HandshakeHackin**: the RX 6000 device-loss fix (#127).
- **BrokeAsh** and **KingKaom**: diagnosing the AMD compiler crash on RX 9070 XT.
- **ParaNyx**: the bench fade report (#124).
- **AMD**: FidelityFX FSR 4; **Microsoft**: DirectX 12 Agility SDK.
- **avatarmanz** and every tester who posted a bench or a log.

**Earlier builds (the `main` code, which other launchers build):**
- [@Marvisak](https://github.com/Marvisak) for [VIctory](https://github.com/Marvisak/VIctory), and [@fxceless](https://github.com/fxceless) (hyphennn) for [victory-fork](https://github.com/fxceless/victory-fork), the base of KLBF Lab.
- [@myokex](https://github.com/myokex) ([victory-amd](https://github.com/myokex/victory-amd)): missing walls on AMD.
- [@Geckomacabre](https://github.com/Geckomacabre) (vx-layer) and [@MiamiGame](https://github.com/MiamiGame) ([XTP](https://github.com/MiamiGame/XTP)): the water physics fix (test builds).
- [@BrokeAsh](https://github.com/BrokeAsh): the RDNA 4 shader compiler workaround; [@gmankab](https://github.com/gmankab) (with AugustoZFJ's original fix): Wine pipeline caching and docs; [@HandshakeHackin](https://github.com/HandshakeHackin): test tools and fixes.
- Upstream VIctory pull requests #334, #1271, #1599 and #1696, and the DirectStorage analysis by JappertjeV.

**Testers and reporters:** [@clems206](https://github.com/clems206), [@TG0000](https://github.com/TG0000), [@BlackBu7let](https://github.com/BlackBu7let), [@kzrts](https://github.com/kzrts), and [@HishamMuhammed](https://github.com/HishamMuhammed), whose questions shaped the [beginner's guide](docs/GUIDE.md).

<details>
<summary><b>Earlier builds on <code>main</code> (Lab 35 to Lab 63, 24–26 Nov 2026)</b></summary>

An open lab that runs the Xbox Series X|S (Scarlett) build of the game natively on a Windows PC: a GDK compatibility layer (`kernelx`, `xgameruntime`, `d3d12_xs` → host D3D12, RDNA2 → DXIL shader translation) that combines the best fixes from open compatibility projects into one tested build. Our own fixes (AMD Radeon stability and rendering, water physics, pre-building pipelines, optional AMD FSR frame generation) and fixes from other contributors, credited below.

> [!TIP]
> **Playing on Linux / Proton?** Our Linux work is led by community member **[@zocram4cc](https://github.com/zocram4cc)**: see his Wine/Proton fixes ([#34](https://github.com/PastiiJay/klbf-lab/pull/34), [#35](https://github.com/PastiiJay/klbf-lab/pull/35)), the [Linux notes in the guide](docs/GUIDE.md#linux--proton-community-notes) and the RX 7800 XT report by [@Adiker](https://github.com/Adiker) ([#19](https://github.com/PastiiJay/klbf-lab/issues/19)). Post Linux results in an issue and tag @zocram4cc.

## New test build: Lab 63 on [`beta-2`](https://github.com/PastiiJay/klbf-lab/tree/beta-2) (26 Nov 2026)

> **AMD beta v12 (27 Nov):** branch [`beta-amd`](https://github.com/PastiiJay/klbf-lab/tree/beta-amd), BM-v1 16.4 fps avg, 1 % low 8.7, 0 freezes on RX 9070 XT (Series X, native) — based on Op-lite's victory-scarlett.
>
> **🧪🌴 New: KLBF Lab Bench · Bayside Morning v1.** A 5-minute hands-off test from the same spot for everyone, input locked, with a certified postcard at the end. [How to run it](docs/klbf/BENCH-BM-V1.md) · [Results by hardware](docs/klbf/BAYSIDE-MORNING-V1.md). Lab 63 also fixes dark faces in shade and skips the intro movie on request.
>
> **Latest run:** 2026-11-27 · **AMD beta v12** ([`beta-amd`](https://github.com/PastiiJay/klbf-lab/tree/beta-amd)), Series X, native · Radeon RX 9070 XT / Ryzen 7 9800X3D · 16.4 fps avg (1 % low 8.7, 0 freezes), BM-v1 certified

> **📏 A shared frame-rate standard.** Numbers between projects cannot be compared today (empty seas, menus, one lucky second). We propose one method for everyone: same starting save, same route, three tables (frame rate seen in the world, stability index, average performance index). **[Read the method](docs/klbf/MEASUREMENT.md)**, use it, and post your numbers.

Lab 61 (the build the figures below were measured on), a test build on the **[`beta-2` branch](https://github.com/PastiiJay/klbf-lab/tree/beta-2)**: correct faces and hair, many more frames per second, and a launcher (`play.ps1`). Measured in a real play session with a controller on an RX 9070 XT 16 GB, Ryzen 7 9800X3D, 32 GB RAM, Series S profile + FSR 4, following the shared method. No cherry-picked numbers: these come from ordinary play.

**Frame rate seen in the world** (peaks by situation)

| Situation | fps |
|---|---|
| Standing still, looking at the sky | up to 27 |
| On foot in a quiet area (by a lake or a river) | up to 23 |
| Standing still in traffic, busy neighbourhood | up to 17 |
| On foot on a motorway slip road | up to 16 |
| On foot in a busy neighbourhood | up to 14 |
| Driving over a bridge above water | up to 17 |
| Driving a truck at moderate speed | up to 15 |
| Driving fast through streets (the world streams in) | up to 12 |

<!-- live-start -->
**Stability index**: how the frame rate is spread over a real play session still running, **37 minutes so far without a crash** (385 samples, on foot and driving; updated every 5 minutes of play):

| fps | Share of the time |
|---|---|
| 18 and more | 16 % |
| 15–18 | 28 % |
| 12–15 | 30 % |
| 9–12 | 15 % |
| 5–9 | 5 % |
| under 5 (freezes) | 6 % |

**Average performance index**, same session: average 14.0 fps, median 14.5, 5 % low 1.8, 1 % low 0.4 (the lows are the freezes).
<!-- live-end -->

Known issues:
- Occasional freezes when the card or PC memory fills (try `-LowMemory`).
- Some shadows flicker near trees; very distant trees sometimes flash black.
- Water surfaces are not drawn (the water is invisible or see-through), and lake water sometimes flickers; swimming still works.
- Mirrors stay black (they need ray tracing).
- Car windows (glass) are not drawn: you can break into a car but the glass is invisible.
- Resolution is Series S, upscaled.


<details>
<summary><b>Older status: Lab 35 (25 Nov 2026), the stable code on this branch</b></summary>

### Status (2026-11-25, Lab 35)

Tested on one machine: AMD Radeon RX 9070 XT 16 GB (Adrenalin 32.0.32029.2010), AMD Ryzen 7 9800X3D, 32 GB RAM, Windows 11. Self-reported, one machine so far.

| Stage | Status | Notes |
|---|---|---|
| Boot, first-run screens, intro, menus | ✅ Works | 30 fps |
| In game | ✅ Player in control | the player controls the character from the prison prologue up to the second character's first mission |
| Frame rate, prologue (prison, in the cell) | ✅ ~7.3 fps | standing in the first character's cell: average 7.34, 1% low 7.0, peak 7.7 over 72 min |
| Frame rate, prologue while playing (cell → office → robbery → arrest) | 🟡 ~5.7 fps | average 5.7, median 5.7, peak 9.4 |
| Frame rate, the second character's first mission (on the boat) | 🟡 ~6.3 fps | average 6.3, median 6.5, peak 9.8 |
| Settings | — | renders at 1280×720 (`--console series-s`), upscaled to 1920×1080 with AMD FSR; dips to ~0.5–1 fps while a new area loads |
| Frame rate in game, native resolution | 🟡 ~5 fps | about 200 ms per frame |
| Stability | ✅ Record: 77 min of play without a crash | on test build Lab 39, stopped by choice to get back to work on the project, not by a crash. This version has never crashed in our tests; we haven't pushed it that far yet |
| Rendering | 🟡 Mostly right | walls, lighting, hair and outfits drawn; purple tint on small flat objects (posters, stickers, towels), some faces deformed (guards, bank), faint diagonal lines on surfaces, the boat sits on the seabed (water physics fixed in test build Lab 39); the HUD (subtitles, objectives, prompts) stays hidden with the recommended settings in this version; fixed in test build Lab 38 (KLBF Lab Beta); at night the vegetation turns magenta and the ground stays very dark |
| Story progress | ✅ Open world reached: prologue and the second character's first mission completed, 3% of the story | played from a new game on our own build, with our own saves (no save file from anyone else): the first character's prologue, then all of the first mission, then free roam from the second character's house, in a 77 min session without a crash (test build Lab 39); autosave and manual saves work, and the bed moves the time between day and night |

> **Stability policy:** we never publish a build that crashed in our tests. Every session length shown here is when **we** stopped, to get back to work on the project or because a test run reached its planned end, not a crash.

#### Why AMD FSR

The recommended settings render the world at 1280×720 and upscale it to 1920×1080 with **AMD FSR** (FidelityFX Super Resolution). The game itself does the same on console: it ships with its own FSR upscaler and calls it every frame. KLBF Lab hands that call to AMD's official FidelityFX SDK on the PC, so the picture is upscaled the way the game expects, and the frame rate goes up by about a third. FSR works on AMD, NVIDIA and Intel cards. Native resolution without FSR is listed too (~5 fps).

</details>

## Built by KLBF Lab

What this project wrote itself, checked commit by commit (everything taken from other forks keeps its credit in [Credits](#credits)):

- **A pipeline pre-build that survives AMD's shader compiler.** On top of the upstream pre-build, KLBF Lab saves progress as it goes (every 200 pipelines and every minute) and resumes after a crash. Pipelines that crash the driver (`amdxc64.dll`) are recorded in `prebuild-crashed.txt`, and every later run skips them. This is what lets the game start on Radeon cards that crash elsewhere.
- **Console wave32 programs on 64-lane AMD hardware.** Each half of a 64-lane wave runs as one console wave, with wave reductions done per half and the console's float-denormal handling. This is the base of correct pixel and vertex shading on RDNA.
- **NaN guard on colour exports and typed stores**, against the purple/black areas one invalid value spreads on AMD. Proposed upstream too: fxceless/victory-fork#837.
- **The console's plane composition.** Each present plane is composed with its own resources, in submission order, scaled the way the console scales it.
- **AMD frame generation (`VICTORY_FRAMEGEN=1`)** through FidelityFX SDK 2.4, with the interface plane handed to the SDK so menus and HUD are not interpolated. Also a no-SDK fallback for the title's upscale (`VICTORY_FFX_SIMPLE=1`).
- **A per-frame budget for texture uploads** (`VICTORY_TEXTURE_QUEUE_MB/MS`), so streaming doesn't stall a frame.
- **Proven in play, on our own saves.** From a new game to the open world: the prologue and the first mission completed, including the water mission with boats floating. The water fix itself is credited to Geckomacabre/vx-layer and MiamiGame/XTP; we integrated and proved it. Record: 77 min of play without a crash.
- **A beginner's guide** ([docs/GUIDE.md](docs/GUIDE.md)) with every command to copy and paste, Windows 10 and Linux notes, and a troubleshooting table built from players' reports.

## Progress

How far the project gets in the story, scene by scene (one machine: AMD Radeon RX 9070 XT, recommended settings with AMD FSR). Frame rates are measured in the world, while playing, unless stated.

| Part of the story | Reached | Frame rate (average / peak) | Notes |
|---|---|---|---|
| Boot, intro video, start screen, menus | ✅ | 30 fps | menus stay black with the recommended settings: press A |
| Prologue: the first character's cell | ✅ | 7.3 standing / 5.7 while playing, peak 9.4 | walls, lighting, outfit right |
| Prologue: the office interview | ✅ | (prologue while playing: 5.7) | faces mostly right, some deformed |
| Prologue: the robbery | ✅ | (prologue while playing: 5.7) | purple stickers on the glass, bank faces deformed |
| Prologue: the escape and the arrest | ✅ | ~4 outside, high-contrast light | the earlier crash point, passed since Lab 33 |
| The second character's first mission: the boat | ✅ (test build Lab 39) | 6.3 / 9.8 | the boat floats and drives since Lab 39; on this version (Lab 35) it sits on the seabed: fail the checkpoint 3 times and the game offers to skip it |
| The first mission: on foot in the swamp, the camp, finding a story character | ✅ | 5.2 average / 12.9 peak (41 min session, test build Lab 38) | first fight works; with Lab 39 the character climbs out of the water normally |
| The first mission: the seaplane, the water landing, the night drive home | ✅ (test build Lab 39) | ~5.2 average / 12.5 peak over the 77 min session; ~9 in flight | mission completed; at night the vegetation turns magenta and the ground stays very dark |
| The second character's house, first manual save | ✅ (test build Lab 39) | — | the bed saves the game; the save menu shows the first mission at 3% |
| Open world (free roam) | ✅ (test builds Lab 39 / Lab 42) | ~5–8 while driving and walking | free roam from the second character's house; sleeping in the bed moves the time on, so day and night can both be tested |
| Further | ⏳ next | — | the next missions |

### Milestones

| Date | Build | Milestone |
|---|---|---|
| 24 Nov 2026 | Lab 03 | in game, black world, ~1 fps, controller works |
| 24 Nov 2026 | Lab 23 | first gameplay scene drawn on AMD, ~2 fps |
| 24 Nov 2026 | Lab 26 | AMD memory leak and purple blocks fixed, ~4.4 fps |
| 25 Nov 2026 | Lab 28 | The first character's face, hair and outfit drawn |
| 25 Nov 2026 | Lab 31 | the cell drawn with its walls |
| 25 Nov 2026 | Lab 35 | 74 min in one session without a crash; prologue ~7.3 fps in the cell |
| 25 Nov 2026 | Lab 37 | played from the prologue to the start of the second character's first mission, peak 9.8 fps |
| 25 Nov 2026 | Lab 38 (test) | menus, map, HUD, subtitles and button prompts show in Series S mode; 41 min of play without a crash; the first mission played up to the seaplane, peak 12.9 fps |
| 25 Nov 2026 | Lab 39 (test) | water physics fixed: the first mission completed, 3% of the story, first manual save, 77 min of play without a crash (stopped by choice, not by a crash); open world reached from a new game |

How we measure: the frame rate the layer logs about every 5 s, in the world only (loading screens and the first 2 minutes of shader compiling left out). Numbers are given per scene: standing in the prison cell, and while actually playing through the prologue and the second character's first mission (18 min session, test build Lab 37). Lows are taken from those 5 s averages, so single-frame dips may go lower.

### Water physics: fixed in test build Lab 39

In test build Lab 39 (the [`beta` branch](https://github.com/PastiiJay/klbf-lab/tree/beta)) the boat in the second character's first mission **floats and moves**: with only the throttle held it sailed over a minute (wake, objectives updating) before hitting the bank. The fix has also been confirmed by another user on an NVIDIA GeForce RTX 5070 Ti (16 GB), in their own build. Our own play-through on Lab 39: the boat, the seaplane take-off and flight (~9 fps) and the water landing all work. It will come to this version once the mission has been played to its end.

Boats, the seaplane and the player in water all behave as if there were no water: the boat rests on the seabed, the seaplane "flies" under the surface. The water itself is drawn right. We think the cause is this: on console the CPU and the GPU share memory, and the game's physics reads back the water height the GPU computes each frame; in our layer that result stayed on the graphics card, so the physics read an empty height map. The next build copies those water textures back into the game's memory (ported from Geckomacabre/vx-layer); fixed in test build Lab 39, together with the XOR swizzle mode the height map is stored in (ported from MiamiGame/XTP).

> [!TIP]
> Until the water physics fix reaches this version: when a water checkpoint fails, fail it **3 times** and the game offers to skip it.

## Community and test reports

The project started on **[KLBF Lab Beta](https://github.com/PastiiJay/klbf-lab-beta)** (13 stars, 2 forks), now archived: test builds moved to this repository's `beta` branch on 25 Nov 2026. Reports from testers there:

- [RX 6900 XT (RDNA2), Windows 10](https://github.com/PastiiJay/klbf-lab-beta/issues/2): runs our builds for 19 min without a device removal; with Lab 33 the player's face renders on that card too; it helped us test two fixes.
- [RX 6800 (RDNA2)](https://github.com/PastiiJay/klbf-lab-beta/issues/4): measured our AMD fixes on that card (same speed with them; purple sky and wet-looking skin gone).
- [DirectStorage page lists](https://github.com/PastiiJay/klbf-lab-beta/issues/3): an analysis by another tester, now part of the build.

No game files are included. You need your own legally obtained copy.

## What it fixes

| Problem | Cause we found | Fix |
|---|---|---|
| Memory grows ~240 MB/s until Windows runs out | compute shader `39f0e9aeb156a61c` never leaves the AMD driver's compiler | skipped |
| Purple/magenta blocks stuck on screen | console 32-lane pixel shaders run in 64-lane waves on AMD; NaN piled up in temporal buffers | 32-lane programs run per half wave; NaN/Inf filtered on colour outputs |
| Missing or late textures | texture upload queue fixed at 192 MB / 250 ms per frame | configurable, larger by default (`VICTORY_TEXTURE_QUEUE_MB`, `VICTORY_TEXTURE_QUEUE_MS`) |
| Characters missing or broken, faces absent | two meshlet-cull compute shaders hung on AMD and had to be skipped | upstream VIctory #334 (buffer-state tracking) ported; `fc5e66f8f873d3bb` no longer skipped: the first character's face, hair and outfit render |
| Compute results not seen by other workgroups | `glc` loads not globally coherent on RDNA | upstream VIctory #1271 ported |
| Lost or misplaced asset loads | DirectStorage page lists read after the title changed them | read at the title's submit (analysis by JappertjeV, [#3](https://github.com/PastiiJay/klbf-lab-beta/issues/3)); `VICTORY_PAGE_LIST=enqueue|submit|late` to compare |
| Cell walls, window frame and posters missing (sky where the wall should be) | pipelines skipped while the world loads, textures streamed in part taken for others | ported from [myokex/victory-amd](https://github.com/myokex/victory-amd): pipelines kept across runs and waited for while a world loads (`VICTORY_PIPELINE_GATE_S`), textures shown from their first loaded mip, lost placed views refreshed (`VICTORY_TEXTURE_SWEEP`), dispatches over 65,535 groups split |
| Walls, window frame and outfit wrong for a whole run, at random | during loading the list of remapped texture ranges overflowed and was thrown away, so which textures got re-checked depended on timing | the list is 32× larger and an overflow triggers a full re-check instead of a drop (found by comparing logs of runs with and without walls) |
| The AMD shader compiler crashes (`amdxc64.dll`) on a few pipelines | driver bug on two pipelines | `victory translate --cache --pipelines` pre-builds every pipeline offline, saves as it goes, finds the crashing ones and skips them in game too |

## What you can expect (tested on an RX 9070 XT, Adrenalin 32.0.32029.2010)

| | Result |
|---|---|
| First cell | walls, window frame, posters and photos drawn; the first character's face, hair and orange outfit render; inmates in the yard |
| Speed, recommended settings (720p upscaled to 1080p with AMD FSR) | **~7.3 fps (median), 74 min with no device removal**, walls drawn throughout |
| Speed, native resolution without FSR | ~4.8–5.2 fps (≈200 ms/frame); 41 min with no device removal (Lab 33) |
| Skipped shaders | only one left (`39f0e9aeb156a61c`, which never leaves the AMD compiler); the other 47 we used to skip now run on this card |
| Cell walls | drawn in 5 of 6 runs (about half before Lab 35). When they are missing, the window frame turns purple and the outfit dark for the whole run; still under investigation |
| Still wrong | a purple tint on some papers and photos, stretched "web" triangles around some characters that change every frame, some textiles look wet, colour banding in skies |

These are a few runs on one machine: other cards and drivers may behave differently.

## Run

> [!IMPORTANT]
> **Before the first run, get AMD's FidelityFX SDK.** The recommended settings (`--console series-s`) use AMD FSR, which needs AMD's DLLs. Download **FidelityFX SDK v2.4.0** from its official page ([GPUOpen-LibrariesAndSDKs/FidelityFX-SDK, releases](https://github.com/GPUOpen-LibrariesAndSDKs/FidelityFX-SDK/releases)), unzip it, and set `VICTORY_FFX_DIR` to its `Kits\FidelityFX\signedbin` folder (it holds `amd_fidelityfx_loader_dx12.dll`). Without it the log says `amd_fidelityfx_loader_dx12.dll not found` and the game crashes once it starts upscaling. No SDK? Run without `--console series-s` (no FSR, slower).

> [!TIP]
> **New to this? Follow the [beginner's guide](docs/GUIDE.md)**: every step is a command to copy and paste, from installing the tools to playing, with a page-file guide and a troubleshooting table.

### Step by step

1. **Install the tools:** [Rust](https://rustup.rs) and Git. You also need your own copy of the game's Xbox Series files on disk, and 32 GB of RAM or a large Windows page file (a run commits about 20 GB).
2. **Get the code and build it:** `git clone https://github.com/PastiiJay/klbf-lab` (or `git clone -b beta https://github.com/PastiiJay/klbf-lab` for the test build), `cd klbf-lab`, then `cargo build --release`. The program is `target\release\victory.exe`.
3. **Get the FidelityFX SDK** (see the box above) for the recommended Series S settings.
4. **Pre-build the pipelines, once.** This compiles all of the game's shaders for your graphics card ahead of time, so the game doesn't stutter or crash on them while you play. It takes about 10 to 20 minutes. If it crashes (the AMD driver sometimes does), just run the same command again: it resumes and remembers the shaders that crashed. Run it again after updating KLBF Lab. Set the same variables as for playing first (step 5), then:

Pre-build command:

```powershell
$env:VICTORY_SHADER_OPT = '0'
$env:VICTORY_SKIP_PIPELINES = (Get-Content docs\klbf\skip-amd.txt -Raw).Trim()
target\release\victory.exe translate --cache --pipelines --jobs 8 <game dir>\shaders.rpf
```

5. **Play** with:

```powershell
$env:VICTORY_SHADER_OPT = '0'
$env:VICTORY_SKIP_PIPELINES = (Get-Content docs\klbf\skip-amd.txt -Raw).Trim()
$env:VICTORY_LATE_WAIT = '1'
$env:VICTORY_WIDE_BACK = '1'
$env:VICTORY_PIPELINE_WAIT_MS = '24'
$env:VICTORY_RELAY_COPY_QUEUE = '0'
$env:VICTORY_FFX_DIR = '<FidelityFX SDK>\Kits\FidelityFX\signedbin'
target\release\victory.exe run --console series-s <game dir>\<the title's exe> --execute
```

`--console series-s` makes the title render at 1280×720, and AMD FSR (from the official [FidelityFX SDK](https://github.com/GPUOpen-LibrariesAndSDKs/FidelityFX-SDK)) upscales it to 1920×1080: that is the ~7 fps setting. Without `--console series-s` the title renders at its native resolution (~5 fps here).

> [!TIP]
> With the recommended settings the start screen and the main menu stay **black**: the title is running behind it. Press **A** on the controller to get past them (the keyboard works on the start screen, but the account picker only answers the controller, [#69](https://github.com/PastiiJay/klbf-lab/issues/69)); the picture appears once the world loads. Plug the controller in **before** starting: plugging it in during play pauses the title.

If the device is lost about a minute after the world starts loading (reported on an RX 9070 non-XT, [#6](https://github.com/PastiiJay/klbf-lab-beta/issues/6)), try `VICTORY_LATE_WAIT=0`.

`VICTORY_SHADER_OPT=0` turns off the fork's shader clean-up passes, which crashed the AMD compiler for us. `VICTORY_TEXTURE_BUDGET_MB=6144` fixed some dark textiles for another tester but hid the cell walls in both our runs with it, so we leave it off for now. 

Please report results in an [issue](https://github.com/PastiiJay/klbf-lab/issues): GPU, driver, how long it ran, fps in the window title, and what looks wrong. Patch notes: [CHANGELOG.md](CHANGELOG.md). Full run log: [docs/klbf/results.md](docs/klbf/results.md).

</details>

KLBF Lab started from [VIctory](https://github.com/Marvisak/VIctory) by Marvisak and the [fxceless/victory-fork](https://github.com/fxceless/victory-fork); it is GPL-3.0 like them, and keeps their copyright notices. Fixes ported from other projects are credited where they are used, above and in the commit messages.

Product names are only used to say what this works with; they belong to their owners. KLBF Lab is not affiliated with them. License: GPL-3.0.
