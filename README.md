# UXUI-Extreme

A coordination and design repository for a personal, modular Windows UI suite. It tracks work and constraints; **there is no executable application or installer in this repository**. Code, CI builds and releases are in the module forks.

The source and binaries are publicly accessible, but the project is personal-use oriented, unsigned and unsupported for general deployment. Follow each fork's upstream licence and the licences of bundled assets.

## Modules

| Module | Fork / implementation | Purpose | Upstream |
|---|---|---|---|
| Taskbar | [RetroBar-Extreme](https://github.com/techrote/RetroBar-Extreme) | Replacement taskbar, labels, tray, style/layout controls | [dremin/RetroBar](https://github.com/dremin/RetroBar) (Apache-2.0) |
| Start menu / Explorer | [Open-Shell-Menu-Extreme](https://github.com/techrote/Open-Shell-Menu-Extreme) | Classic Start menu, selected Explorer integration | [Open-Shell/Open-Shell-Menu](https://github.com/Open-Shell/Open-Shell-Menu) (MIT) |
| Whole-window skins | Not started | Potential future module | Not selected |

## Verified delivery baseline

As of **4 November 2026**, RetroBar-Extreme's latest verified published release is **[v1.23.43-extreme-delta.1](https://github.com/techrote/RetroBar-Extreme/releases/tag/v1.23.43-extreme-delta.1)** (published 18 October from `master` `65b36c0`).

- [Download RetroBar-Extreme portable ZIP](https://github.com/techrote/RetroBar-Extreme/releases/download/v1.23.43-extreme-delta.1/RetroBar-Extreme-Portable.zip) — contains multiple platform builds; select the appropriate Windows build folder.
- [Release notes and other downloads](https://github.com/techrote/RetroBar-Extreme/releases/tag/v1.23.43-extreme-delta.1) — installer and Extras package.
- [Latest verified RetroBar build run](https://github.com/techrote/RetroBar-Extreme/actions/runs/39116769177) — source-bound CI success, **not** a visual qualification.

The fork includes native sizing, fonts and clock controls, colour and texture editing, saved styles, per-app task-button overrides, Start/Quick and Icons controls, and task-row layout. See [the programme](docs/PROGRAMME.md) for feature provenance and [the parity checklist](docs/PARITY.md) for remaining gaps.

## Testing and recovery

RetroBar-Extreme replaces the taskbar **as a separate application**, not by injecting a replacement Explorer taskbar. On the documented configuration, closing RetroBar returns the standard Windows taskbar. Try an unsigned portable release cautiously and ensure normal taskbar recovery on the target Windows build. Some Open-Shell/Explorer integration changes require a snapshotted VM before real-machine testing. Portable builds may require the Microsoft .NET Desktop Runtime.

A successful GitHub Actions build establishes compilation/test results, not good appearance or behaviour on the owner's screen. Release notes may report owner use; feature-specific visual acceptance must be recorded separately.

## Repository navigation

- [PROGRAMME.md](docs/PROGRAMME.md) — current milestones, accepted implementation and planned phases.
- [PARITY.md](docs/PARITY.md) — StartAllBack feature comparison, with evidence levels.
- [STYLE-ENGINE.md](docs/STYLE-ENGINE.md) and [STYLE-MAP.md](docs/STYLE-MAP.md) — design history and theme-resource mapping.
- [RAG.md](RAG.md) — current engineering facts, decisions and baselines.
- [AGENTS.md](AGENTS.md) — engineering, acceptance and safety rules.
- [Audit / remediation record](docs/AUDIT-2026-11-04.md) — findings, fixes and residual risks.
- [Cross-module tracker](https://github.com/techrote/UXUI-Extreme/issues/6) — UX-018.

Implementation issues belong in the module forks. Older umbrella issues #1–4 are closed historical copies and should not be mistaken for active module defects.

## Repository checks

Documentation changes are checked for broken local links and heading anchors in GitHub Actions. To reproduce locally with Python 3.11+:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/check_docs.py
```

These offline checks cannot prove that remote module status is current, that a build runs on Windows, or that the owner has accepted its visuals.
