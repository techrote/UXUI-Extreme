# Programme

Order of work. Issues carry the detail; this page is the map.

## Phase 0 — Workshop *(in progress)*

- Umbrella repo, rules and checklist. ✅
- Confirm CI builds portable zips for PRs on RetroBar-Extreme.
- Windows 11 test VM with snapshots — needed before any Explorer-injecting work (Open-Shell, skinning), not for RetroBar.

## Phase 1 — Make RetroBar feel right *(current)*

The owner's first-impression fixes, in this order:

| ID | What | Why this order |
|---|---|---|
| [UX-001](https://github.com/techrote/UXUI-Extreme/issues/1) | Tray icons stuck inverted | Small, clear bug; proves the build → test → merge loop end to end |
| [UX-002](https://github.com/techrote/UXUI-Extreme/issues/2) | Crisp pixel-style text at non-integer scaling | Perceptual; needs side-by-side prototypes the owner compares |
| [UX-003](https://github.com/techrote/UXUI-Extreme/issues/3) | Style layer: custom colours, gradients and fonts over any theme | Builds on what UX-002 decides about fonts |
| [UX-004](https://github.com/techrote/UXUI-Extreme/issues/4) | Style editor in RetroBar's Properties window | Needs the UX-003 layer to edit |

## Phase 2 — Taskbar parity with the owner's StartAllBack setup

Checklist-driven from [PARITY.md](PARITY.md): Start button opening the Open-Shell menu, label/width behaviour, thumbnails and jump lists, multi-monitor, auto-hide modes.

## Phase 3 — Start menu and Explorer gaps (Open-Shell-Menu-Extreme)

## Phase 4 — Extreme extras

Ratrod skin pack, whole-window skinning module, anything StartAllBack never had.
