# RAG — UXUI-Extreme

Compact development context. **Module facts were checked on 4 November 2026**, against RetroBar `65b36c0fba6ef8d8e44294b3ea332b03e32f638c` and Open-Shell `e1fe220d18bb38a0d8a19c70332d75fef4c2625f`. The [audit record](docs/audits/2026-11-04-quality-audit.md) links source, CI and acceptance evidence. Read live state before changing a module; reconcile conflicts here and in [PROGRAMME](docs/PROGRAMME.md).

## Goal and scope

Replace StartAllBack on the owner's machines with a suite we control, then extend it. This repository is the coordination/documentation hub. Application implementation belongs in the module forks; no Windows application is built by this repository's documentation CI.

## Target system and owner observations

- Windows 11 is the target. **26H2, build 26300.9457** was an owner-reported October 2026 test environment, not a current-machine inventory or proof of compatibility. Record the actual OS build, Windows DPI, taskbar scale and module versions for each new visual/recovery test; do not hard-code this build into behavior.
- Historical October setup: 5600X/Titan RTX + V100, 2600X/K80, E5-2686 v4/RTX 4000 and i7-6700/Quadro M620. Hardware allocations can change; ask only if a concrete test needs a missing detail.
- Taskbar priorities: slim, small icons, labelled window buttons, never-combined, pinned shortcuts, compact tray and clock. Middle-click and Win+number were already liked in stock RetroBar.
- The [12 October report](https://github.com/techrote/RetroBar-Extreme/issues/11#issuecomment-6128686146) used 100% taskbar scale, Orbitron Hinted 17px/600 and row height adjust −4. The later [clock acceptance](https://github.com/techrote/RetroBar-Extreme/issues/13#issuecomment-6130777321) used row height adjust 0 for the XP-family test. These are observations, not universal defaults.
- Look: industrial, down-to-earth, non-neon "ratrod" cyberpunk; function over form. Pixel-style system fonts are welcome. Historical font comparisons are specific to those files, sizes and screens, not a guarantee about every font called Orbitron or every DPI.

## Decisions

| ID | Decision | Boundary |
|---|---|---|
| D-001 | Separate-process replacement taskbar using RetroBar | Avoid introducing Explorer injection into the taskbar module. This reduces coupling; it does not guarantee compatibility with every Windows update or prove crash recovery. |
| D-002 | Modular forks, one umbrella | Module issues/PRs own implementation; this repository owns the overview and cross-module evidence. Keep changes mergeable with upstream. |
| D-003 | Personal use | No signing, telemetry, automatic updater traffic or store packaging. Public personal prerelease packages already exist. Preserve upstream and asset licenses/notices; do not erase this policy to match inherited code. |
| D-004 | No reverse engineering of commercial products | Use open-source references and Microsoft documentation. |
| D-005 | Native sizing is the taskbar default; stretch remains selectable | Native sizing avoids whole-taskbar stretch, while Windows DPI still applies. Whole-number WPF layout sizes are not a promise of single physical pixels. See [STYLE-ENGINE](docs/STYLE-ENGINE.md). |

These decisions date from 12 October 2026; the wording above distinguishes intent from verified implementation. Current policy gaps are listed below.

## RetroBar-Extreme: implemented source

- C#/WPF; `RetroBar/RetroBar.csproj` targets `net6.0-windows` and `net10.0-windows`. ManagedShell supplies tray/task-list plumbing. [Project source](https://github.com/techrote/RetroBar-Extreme/blob/65b36c0fba6ef8d8e44294b3ea332b03e32f638c/RetroBar/RetroBar.csproj).
- Native sizing is the default in `Utilities/Settings.cs`. `ScaleModel` gives the native path a unit taskbar transform and scales the loaded theme; stretch mode applies the whole-bar transform. Text and theme helpers handle the selected mode. [ScaleModel](https://github.com/techrote/RetroBar-Extreme/blob/65b36c0fba6ef8d8e44294b3ea332b03e32f638c/RetroBar/Utilities/ScaleModel.cs).
- Themes are XAML resource dictionaries in `RetroBar/Themes/`; `System.xaml` loads first, then the selected theme, then overrides. Custom themes can be found in `%LOCALAPPDATA%\RetroBar\Themes\` or beside the executable. [DictionaryManager](https://github.com/techrote/RetroBar-Extreme/blob/65b36c0fba6ef8d8e44294b3ea332b03e32f638c/RetroBar/Utilities/DictionaryManager.cs).
- `settings.json`, `Style.json` and named `Styles\` files live under `%LOCALAPPDATA%\RetroBar\`, including when a portable executable is used. A portable test is not an isolated settings sandbox. [Path helper](https://github.com/techrote/RetroBar-Extreme/blob/65b36c0fba6ef8d8e44294b3ea332b03e32f638c/RetroBar/Extensions/ManagementExtensions.cs).
- Style files save brush/texture part overrides, a 12-slot colour palette, a 20-slot texture palette, Start recolouring and per-part border factors. Theme, fonts and layout remain application settings; exporting a style is not a full configuration backup. [StyleDocument](https://github.com/techrote/RetroBar-Extreme/blob/65b36c0fba6ef8d8e44294b3ea332b03e32f638c/RetroBar/Utilities/StyleDocument.cs), [Start](https://github.com/techrote/RetroBar-Extreme/blob/65b36c0fba6ef8d8e44294b3ea332b03e32f638c/RetroBar/Utilities/StyleDocument.Start.cs), [borders](https://github.com/techrote/RetroBar-Extreme/blob/65b36c0fba6ef8d8e44294b3ea332b03e32f638c/RetroBar/Utilities/StyleDocument.Borders.cs).
- UX-017 embeds 24 font families and provides example styles/Extras. This does not implement the earlier arbitrary private `Fonts\` directory proposal. [BundledFonts](https://github.com/techrote/RetroBar-Extreme/blob/65b36c0fba6ef8d8e44294b3ea332b03e32f638c/RetroBar/Utilities/BundledFonts.cs), [PR #30](https://github.com/techrote/RetroBar-Extreme/pull/30).
- Tray inversion still uses `InvertIconsMode`, per-icon selection and the theme's `InvertSystemNotifyIcons`. Automatic background-brightness selection remains proposed. Generated colour schemes perform limited contrast selection; there is no general contrast-warning feature for every user style. [NotifyIcon](https://github.com/techrote/RetroBar-Extreme/blob/65b36c0fba6ef8d8e44294b3ea332b03e32f638c/RetroBar/Controls/NotifyIcon.xaml.cs), [Colourways](https://github.com/techrote/RetroBar-Extreme/blob/65b36c0fba6ef8d8e44294b3ea332b03e32f638c/RetroBar/Utilities/Colourways.cs).
- Explicit Open-Shell recognition/menu-placement paths exist. The exact two-module pair still needs Windows qualification. [StartMenuMonitor](https://github.com/techrote/RetroBar-Extreme/blob/65b36c0fba6ef8d8e44294b3ea332b03e32f638c/RetroBar/Utilities/StartMenuMonitor.cs).

## Builds and outstanding policy gaps

| Module | Inspected build behavior | Qualification boundary |
|---|---|---|
| RetroBar | `.github/workflows/retrobar.yml`: push/PR to `master`, `windows-2025`, installers and architecture-specific/aggregate portable artifacts. Normal Windows 11 portable artifacts target .NET 10 and are framework-dependent; matching Desktop Runtime is required. | Build and three contract workflows passed at `65b36c0`. Historical owner acceptance does not certify that entire head. See [build guide](docs/BUILD-AND-TEST.md). |
| Open-Shell | C++/ATL/Win32, VS 2022, `Src/OpenShell.sln`. `.github/workflows/build.yml`: path-filtered PRs to `master` and manual dispatch, `windows-2022`; installer/symbols/utility outputs. No push trigger. | No visible fork CI run or release in the audit. Manual dispatch on `master` includes signing and prerelease publication. It is not a qualified build-only route. |

**UX-019:** RetroBar's inspected default branch still contains automatic upstream update checks, including an installer probe. [The repair issue](https://github.com/techrote/RetroBar-Extreme/issues/34) tracks the separately reviewed module change; until that change is accepted, do not describe existing builds as satisfying the no-updater policy. Turning off **Check for updates** mitigates application polling on the old build, not the installer's probe.

**UX-020:** Open-Shell includes an updater enabled by default in its inherited installer/code. [The module prerequisite](https://github.com/techrote/Open-Shell-Menu-Extreme/issues/1) covers unsigned non-publishing CI, updater policy, exact artifacts and snapshot-VM install/exit/uninstall/recovery qualification. Explorer cleanup code is not proof that recovery works on the owner's current Windows build.

## Next-action routing

- Programme and task ownership: [PROGRAMME](docs/PROGRAMME.md).
- Current capabilities and remaining acceptance: [PARITY](docs/PARITY.md).
- Implemented styling versus proposals: [STYLE-ENGINE](docs/STYLE-ENGINE.md) and [STYLE-MAP](docs/STYLE-MAP.md).
- Exact source/build/owner-report evidence: [4 November audit](docs/audits/2026-11-04-quality-audit.md).
- Agent behavior and merge gates: [AGENTS](AGENTS.md).
