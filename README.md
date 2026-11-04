# UXUI-Extreme

A personal, modular Windows 11 UI-modding suite: a StartAllBack replacement first, then whatever else Windows should have let us change.

This repository holds the plan, evidence and development rules. The Windows applications live in the module repositories below. Public fork repositories and prerelease downloads exist for personal testing; this is not a supported general-purpose distribution.

## How it fits together

Each implemented module is a fork of an existing open-source project, kept close to its upstream so fixes can be integrated. Module issues own implementation details; this repository tracks their relationships and suite-wide work.

| Module | Repo | Job | Upstream |
|---|---|---|---|
| Taskbar | [RetroBar-Extreme](https://github.com/techrote/RetroBar-Extreme) | Replacement taskbar: labels, tray, clock, themes | [dremin/RetroBar](https://github.com/dremin/RetroBar) (Apache-2.0, C#/WPF) |
| Start menu | [Open-Shell-Menu-Extreme](https://github.com/techrote/Open-Shell-Menu-Extreme) | Classic Start menu; Explorer toolbar/status bar | [Open-Shell/Open-Shell-Menu](https://github.com/Open-Shell/Open-Shell-Menu) (MIT, C++) |
| Window skins | not started | WindowBlinds-style whole-window theming | to be chosen |

**State checked 4 November 2026:** RetroBar's UX-001–017 implementations are merged; UX-002 follow-up remains open. Its build and three contract workflows passed at `65b36c0`. Open-Shell source was inspected at `e1fe220`, but no fork CI run or release was returned. An unsigned, non-publishing build, updater-policy changes and VM recovery qualification remain prerequisites. The [audit record](docs/audits/2026-11-04-quality-audit.md) supplies exact commits, runs and historical owner reports. Recheck live state before new work; compilation does not establish new owner acceptance.

## Where things are

- **What we're doing and in what order:** [docs/PROGRAMME.md](docs/PROGRAMME.md)
- **StartAllBack feature checklist:** [docs/PARITY.md](docs/PARITY.md)
- **How the taskbar's look is controlled (design):** [docs/STYLE-ENGINE.md](docs/STYLE-ENGINE.md)
- **Which theme resources the colour layer changes:** [docs/STYLE-MAP.md](docs/STYLE-MAP.md)
- **Build downloads, prerequisites and test handoff:** [docs/BUILD-AND-TEST.md](docs/BUILD-AND-TEST.md)
- **Work items:** detailed issues live in each module repo ([RetroBar-Extreme](https://github.com/techrote/RetroBar-Extreme/issues), [Open-Shell-Menu-Extreme](https://github.com/techrote/Open-Shell-Menu-Extreme/issues)). This repo keeps the overview; its own issues are only for work spanning several modules.
- **Rules for agents:** [AGENTS.md](AGENTS.md), then [RAG.md](RAG.md)

## Trying a build

**RetroBar:** use the exact portable artifact named on the work item. The [inspected x64 CI artifact](https://github.com/techrote/RetroBar-Extreme/actions/runs/39116769177/artifacts/12132522901) is named **RetroBar Portable 64-bit**, built from `65b36c0`. It needs the matching **.NET 10 Desktop Runtime for Windows x64**; portable describes the application packaging, not an absence of runtime or saved settings. Read the [build guide](docs/BUILD-AND-TEST.md) before replacing a daily build.

**Open-Shell:** do not use the RetroBar instructions. Its inherited workflow produces an installer and has not been qualified for this suite. [UX-020](https://github.com/techrote/Open-Shell-Menu-Extreme/issues/1) tracks unsigned, non-publishing builds, updater removal and snapshot-VM installation/recovery checks. The owner is not expected to build it.

## Repository checks

The [documentation workflow](.github/workflows/docs-quality.yml) checks local links and anchors on pull requests and pushes. Agents can run the same checks with Python 3.10 or later; no third-party packages or network access are needed:

```bash
python3 scripts/check_docs.py
python3 -m unittest discover -s tests -v
```

These checks protect document navigation. They do not verify remote links, live GitHub status, module compilation or Windows behavior. Update [PROGRAMME](docs/PROGRAMME.md), [PARITY](docs/PARITY.md) and the relevant evidence together when module state changes.

The public `scripts/check_docs.py` entry point delegates to the shared implementation in `tools/check_docs.py`. The [initial audit merged in PR #7](docs/AUDIT-2026-11-04.md) is retained as history; the [extended audit](docs/audits/2026-11-04-quality-audit.md) records the additional findings and integration.
