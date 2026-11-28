# Check your download, or build it yourself

## 1. Check the zip you downloaded

Each release has **two zips with two different fingerprints** (SHA-256). Compare the one you downloaded,
with the table on the [release page](https://github.com/PastiiJay/klbf-lab/releases/latest):

| File | For |
|---|---|
| `KLBF-Lab.zip` | people: the files inside a "KLBF Lab" folder |
| `KLBF-Lab-win64.zip` | the automatic update: the same files, no folder |

In PowerShell, in the folder of the zip:

```
Get-FileHash .\KLBF-Lab.zip -Algorithm SHA256
```

The `Hash` it prints must be the one next to `KLBF-Lab.zip` (upper or lower case does not matter).
GitHub also shows each file's SHA-256 under **Assets** on the release page.

## 2. Check a folder you already extracted

A folder has no single fingerprint: check the files one by one. `SHA256SUMS.txt`, inside the folder, lists
every file. In PowerShell, inside the "KLBF Lab" folder:

```
Get-Content SHA256SUMS.txt | % { $h,$f = $_ -split ' \*',2; if ((Get-FileHash -LiteralPath $f -Algorithm SHA256).Hash -ne $h) { "DIFFERENT: $f" } else { "ok: $f" } }
```

Every line must say `ok`. After the first start the folder also holds files that are not in the list
(`D3D12\`, `ffx\`, shaders, settings): that is normal.

## 3. Updates

**Update** in the launcher downloads `KLBF-Lab-win64.zip`, checks it against the SHA-256 written in the release
notes, and changes nothing if it does not match.

## 4. Build it yourself

Prerequisites: Windows 10 or 11 (64-bit), Rust with [rustup](https://rustup.rs), Visual Studio 2022 Build
Tools ("Desktop development with C++"), Git. In PowerShell:

```
git clone --branch v26.11.5 https://github.com/PastiiJay/klbf-lab
cd klbf-lab
rustup toolchain install
cargo build --profile diag --features diagnostics --locked -p victory
powershell -ExecutionPolicy Bypass -File scripts\package-release.ps1 -Tag v26.11.5 -Victory target\diag\victory.exe -Out .\dist
```

The same commands as our release workflow (`.github/workflows/release.yml`). You get `dist\KLBF-Lab.zip` and
`dist\KLBF-Lab-win64.zip`. Replace `v26.11.5` with the version you want.

Your build will **not** have the same fingerprint as ours (paths, timestamps and toolchain details end up in the
exe): compare how it behaves, not its hash. The scripts (`play.ps1`, `launcher-menu.ps1`) are copied as they
are, so theirs match `SHA256SUMS.txt`.
