# UXUI-Extreme

A personal, modular Windows 11 UI-modding suite: a StartAllBack replacement first, then whatever else Windows should have let us change.

Built for one user and their machines. Not published, signed or supported for anyone else.

## How it fits together

Each piece is a fork of an existing open-source project, kept as close to its upstream as practical so we can keep pulling in their fixes. This repo is the glue: the plan, the rules, the feature checklist and the issue tracker for all of them.

| Module | Repo | Job | Upstream |
|---|---|---|---|
| Taskbar | [RetroBar-Extreme](https://github.com/techrote/RetroBar-Extreme) | Replacement taskbar: labels, tray, clock, themes | [dremin/RetroBar](https://github.com/dremin/RetroBar) (Apache-2.0, C#/WPF) |
| Start menu | [Open-Shell-Menu-Extreme](https://github.com/techrote/Open-Shell-Menu-Extreme) | Classic Start menu; Explorer toolbar/status bar | [Open-Shell/Open-Shell-Menu](https://github.com/Open-Shell/Open-Shell-Menu) (MIT, C++) |
| Window skins | not started | WindowBlinds-style whole-window theming | to be chosen |

## Where things are

- **What we're doing and in what order:** [docs/PROGRAMME.md](docs/PROGRAMME.md)
- **StartAllBack feature checklist:** [docs/PARITY.md](docs/PARITY.md)
- **How the taskbar's look is controlled (design):** [docs/STYLE-ENGINE.md](docs/STYLE-ENGINE.md)
- **Work items:** detailed issues live in each module repo ([RetroBar-Extreme](https://github.com/techrote/RetroBar-Extreme/issues), [Open-Shell-Menu-Extreme](https://github.com/techrote/Open-Shell-Menu-Extreme/issues)). This repo keeps the overview; its own issues are only for work spanning several modules.
- **Rules for agents:** [AGENTS.md](AGENTS.md), then [RAG.md](RAG.md)

## Trying a build

Every pull request to a module builds automatically on GitHub's Windows servers. Open the PR, follow its **Checks** link, and download the `portable` zip from the run's **Artifacts** section. Unzip anywhere and run; no install. Quit RetroBar from its tray/right-click menu and the normal Windows taskbar comes back.
