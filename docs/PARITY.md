# StartAllBack parity checklist

**Reconciled 4 November 2026** against the [RetroBar-Extreme delta 1 release](https://github.com/techrote/RetroBar-Extreme/releases/tag/v1.23.43-extreme-delta.1), [current `master`](https://github.com/techrote/RetroBar-Extreme/commit/65b36c0fba6ef8d8e44294b3ea332b03e32f638c) and [module README](https://github.com/techrote/RetroBar-Extreme). This is a capability inventory, **not** a physical test matrix or a claim of full StartAllBack compatibility.

**Legend:** ✅ implemented or documented in current fork; 🟡 partly implemented or behaviour not qualified; ❌ missing/not known implemented; ❓ not checked on the target build. The mark does not itself mean owner visual PASS. ★ denotes the owner's known priority.

## Taskbar — RetroBar-Extreme

| Feature | Current fork status | Evidence / remaining qualification |
|---|---|---|
| ★ Window titles on task buttons | ✅ stock RetroBar | Validate long titles, high DPI and multiple monitors |
| ★ Never combine window buttons | ✅ stock RetroBar | Optional future grouping only |
| ★ Slim bar, small icons and geometry controls | 🟡 native scale, row adjustments, layout, button widths | No blanket assertion that every icon/tray size is independently controllable |
| ★ Crisp text at awkward scaling | ✅ native sizing default; sharp stretch modes available | [UX-002](https://github.com/techrote/RetroBar-Extreme/issues/3), [UX-006](https://github.com/techrote/RetroBar-Extreme/issues/9); font-specific results vary |
| ★ Custom fonts (family, size, weight, italic, spacing) | ✅ controls and 24 built-in fonts | [UX-005](https://github.com/techrote/RetroBar-Extreme/issues/7), [UX-017](https://github.com/techrote/RetroBar-Extreme/issues/29) |
| ★ Custom colours, gradients, textures and borders | ✅ style layer/editor, per-part controls | [UX-003](https://github.com/techrote/RetroBar-Extreme/issues/4), [UX-004](https://github.com/techrote/RetroBar-Extreme/issues/5), [delta 1](https://github.com/techrote/RetroBar-Extreme/releases/tag/v1.23.43-extreme-delta.1) |
| ★ Live tray icon inversion settings | ✅ stale inversion effect fixed | [UX-001](https://github.com/techrote/RetroBar-Extreme/issues/2); automatic brightness-based inversion still only a design proposal |
| ★ Global and per-app task-button widths/icons/labels | ✅ persisted options | [UX-014](https://github.com/techrote/RetroBar-Extreme/issues/26), merged [PR #24](https://github.com/techrote/RetroBar-Extreme/pull/24) |
| ★ Vertical Start and clock, Show Desktop placement | ✅ Layout/Start-Quick controls | [UX-012](https://github.com/techrote/RetroBar-Extreme/issues/22), [delta 1](https://github.com/techrote/RetroBar-Extreme/releases/tag/v1.23.43-extreme-delta.1) |
| ★ Custom PNG Start, quick launch and tray controls | ✅ Icons/Start-Quick controls | [UX-015](https://github.com/techrote/RetroBar-Extreme/issues/27), [UX-016](https://github.com/techrote/RetroBar-Extreme/issues/28), delta release |
| ★ Per-row app layout, alignment and height | ✅ added by delta polish | [Delta 1](https://github.com/techrote/RetroBar-Extreme/releases/tag/v1.23.43-extreme-delta.1) |
| Middle-click task buttons and Win+number hotkeys | ✅ stock, previously owner-liked | Check regressions against module build |
| Move taskbar to top/left/right | ✅ stock RetroBar Edge | Vertical Start/clock rotation is not claimed applicable on side bars |
| Multi-row taskbar / adjustable width | ✅ stock rows and fork layout controls | Verify row wrapping with extreme scales |
| Window thumbnails on hover | ✅ stock option `ShowTaskThumbnails` | Qualify parity with StartAllBack |
| Drag files onto task buttons / reorder | 🟡 stock button reorder; Quick Launch drop improved | File-drop-to-running-app behaviour not verified |
| Multi-monitor taskbars | ✅ stock `ShowMultiMon` / `MultiMonMode` | No full real-world DPI/mixed-monitor acceptance on record here |
| Taskbar auto-hide | 🟡 plain auto-hide | Maximise-only auto-hide unverified |
| Start button opens Open-Shell menu | ❓ | Phase 2 integration test required |
| Jump lists | ❓ | Phase 2 behaviour test required |
| Centred task icons while Start stays left | ❌ not established | Future work |
| Segmented / transparent floating bar | 🟡 stock blur and style control | No true Aura equivalent demonstrated |
| Clock seconds / custom text | ✅ stock format plus fork clock control | Inspect target clock formatting |
| Unread-count badges | ✅ stock `ShowTaskBadges` | Physical check as needed |
| Volume by wheel over tray | ✅ stock | Physical check as needed |
| Mic mute by middle-click | ❌ not established | Potential Phase 2 |
| Network/battery/volume flyouts | ❓ stock uses Windows integration | Qualify on target Windows build |

## Start menu — Open-Shell-Menu-Extreme

| Feature | Current assessment | Evidence / work |
|---|---|---|
| Classic one-click cascading menus | ✅ upstream capability | Verify fork behaviour on target build |
| Fast search and configurable menu icons | ✅ upstream capability | Verify on 26H2 |
| Start button integration with RetroBar | ❓ not qualified | Phase 2 cross-module acceptance |

## Explorer / system UI

| Feature | Current assessment | Evidence / work |
|---|---|---|
| Ribbon/command-bar choice | ❌ not established | Phase 3 |
| Details pane at bottom | ❌ not established | Phase 3 |
| Classic search box | ❌ not established | Phase 3 |
| Explorer toolbar/status bar | 🟡 upstream Open-Shell ClassicExplorer capability | Target build compatibility and recovery require VM test |
| Dark-mode dialogs | ❌ not established | Future work |
| Restyled context menus | ❌ not established | Future work |
| Whole-window skins | ❌ no chosen module | Phase 4 proposal |

Release notes describe daily owner use of delta 1 but do not establish independent acceptance of every unchecked feature. Maintain real-world evidence in the corresponding module issue before changing an unchecked status to verified.
