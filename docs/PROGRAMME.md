# Programme

Order of work across all modules. Detailed instructions and progress live in each module's issues (linked); this page is the map.

## Phase 0 — Workshop *(in progress)*

- Umbrella repo, rules and checklist. ✅
- Confirm CI builds portable zips for PRs on RetroBar-Extreme. ✅
- Windows 11 test VM with snapshots — needed before any Explorer-injecting work (Open-Shell, skinning), not for RetroBar.

## Phase 1 — Make RetroBar feel right *(current)*

Releases: [v1.23.31-extreme-alpha.1](https://github.com/techrote/RetroBar-Extreme/releases/tag/v1.23.31-extreme-alpha.1) (UX-001, 002, 005–008) · [v1.23.32-extreme-alpha.2](https://github.com/techrote/RetroBar-Extreme/releases/tag/v1.23.32-extreme-alpha.2) (+ UX-003 style layer).

The owner's first-impression fixes, in this order:

| ID | What | Why this order |
|---|---|---|
| [UX-001](https://github.com/techrote/RetroBar-Extreme/issues/2) | Tray icons stuck inverted · ✅ *merged ([PR #1](https://github.com/techrote/RetroBar-Extreme/pull/1)), owner-tested; inversion defaults deferred to UX-003* | Small, clear bug; proves the build → test → merge loop end to end |
| [UX-002](https://github.com/techrote/RetroBar-Extreme/issues/3) | Crisp pixel-style text at non-integer scaling · *opt-in mode merged ([PR #6](https://github.com/techrote/RetroBar-Extreme/pull/6)); default decided after fonts* | Perceptual; needs side-by-side prototypes the owner compares |
| [UX-005](https://github.com/techrote/RetroBar-Extreme/issues/7) | Font settings over any theme (family, size, weight, italic) · ✅ *merged ([PR #8](https://github.com/techrote/RetroBar-Extreme/pull/8)), owner-tested* | Owner pulled forward: native-size text needs a font chosen for that size |
| [UX-006](https://github.com/techrote/RetroBar-Extreme/issues/9) | Native sizing: draw at real size, no stretching (style engine S2) · ✅ *merged ([PR #10](https://github.com/techrote/RetroBar-Extreme/pull/10)), owner-tested* | Owner decision: native sizing is the default and target |
| [UX-007](https://github.com/techrote/RetroBar-Extreme/issues/11) | Text fixes: menus, symbol fonts, row height + manual adjust · ✅ *merged ([PR #12](https://github.com/techrote/RetroBar-Extreme/pull/12)), owner-tested* | Found while testing UX-006 |
| [UX-008](https://github.com/techrote/RetroBar-Extreme/issues/13) | Line spacing, clock lines/fit/position, steady clock width (clock overflow + walking divider) · ✅ *merged ([PR #14](https://github.com/techrote/RetroBar-Extreme/pull/14)), owner-tested* | Found in daily use |
| [UX-003](https://github.com/techrote/RetroBar-Extreme/issues/4) | Style layer: custom colours and gradients over any theme · ✅ *merged ([PR #15](https://github.com/techrote/RetroBar-Extreme/pull/15)), owner-tested; map in [STYLE-MAP.md](STYLE-MAP.md)* | Fonts now handled by UX-005 |
| [UX-004](https://github.com/techrote/RetroBar-Extreme/issues/5) | Style editor in RetroBar's Properties window (Colours tab) · *in PR ([PR #16](https://github.com/techrote/RetroBar-Extreme/pull/16)), agent-tested; awaiting owner test* | Needs the UX-003 layer to edit |
| [UX-009](https://github.com/techrote/RetroBar-Extreme/issues/17) | Colourways: copy/paste on colours, 12-slot floating palette, generated button/tray schemes, presets | Owner request after UX-004; makes whole colour sets quick |
| [UX-010](https://github.com/techrote/RetroBar-Extreme/issues/18) | Start button colourways: colours from the Start button graphic, and recolouring it to match | Builds on the UX-009 palette and scheme generator |
| [UX-011](https://github.com/techrote/RetroBar-Extreme/issues/19) | *Stretch:* textures coloured from a LUT (brushed metal, carbon, scanlines…) | Needs UX-009 palettes; Phase 4 skin-pack groundwork |

> **Style engine design pass:** [STYLE-ENGINE.md](STYLE-ENGINE.md) proposes one engine for sizes, fonts, icons and colours, and reorders the rest of Phase 1 into slices S1–S7. *Decision A (native sizing) taken; B and order open.*

## Phase 2 — Taskbar parity with the owner's StartAllBack setup

Checklist-driven from [PARITY.md](PARITY.md): Start button opening the Open-Shell menu, label/width behaviour, thumbnails and jump lists, multi-monitor, auto-hide modes.

## Phase 3 — Start menu and Explorer gaps (Open-Shell-Menu-Extreme)

## Phase 4 — Extreme extras

Ratrod skin pack, whole-window skinning module, anything StartAllBack never had.
