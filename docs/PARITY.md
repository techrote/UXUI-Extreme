# StartAllBack parity checklist

What StartAllBack does, whether stock RetroBar / Open-Shell already covers it, and what we plan. Owner priorities are marked ★.

Status key: ✅ have it · 🟡 partly · ❌ missing · ❓ unchecked. "Stock" means unmodified upstream, as read from its settings and code (not yet owner-tested unless noted).

## Taskbar (RetroBar-Extreme)

| Feature | Stock | Plan |
|---|---|---|
| ★ Labels with window titles | ✅ | — |
| ★ Never combine (one button per window) | ✅ RetroBar doesn't group | Optional grouping later, if wanted |
| ★ Slim bar / small icons / adjustable size | 🟡 overall scale only (`TaskbarScale`) | Separate icon size, margins, button width |
| ★ Crisp text when scaled | 🟡 opt-in native-size mode (owner: better; font choice next) | [UX-002](https://github.com/techrote/RetroBar-Extreme/issues/3) |
| ★ Custom fonts (family, size, weight) | ❌ theme XAML only | [UX-005](https://github.com/techrote/RetroBar-Extreme/issues/7) |
| ★ Custom colours, gradients | 🟡 hand-written theme XAML only | [UX-003](https://github.com/techrote/RetroBar-Extreme/issues/4) |
| ★ Tray icon colour inversion settings work | 🟡 works once icons are ticked by hand; defaults don't match 26H2 (owner-tested) | UX-001 ✅; defaults in [UX-003](https://github.com/techrote/RetroBar-Extreme/issues/4) |
| Middle-click, Win+number hotkeys | ✅ (owner-liked) | — |
| Move to top/left/right edge | ✅ `Edge` | — |
| Multi-row / width | ✅ `RowCount`, `TaskbarWidth` | — |
| Start button opens Open-Shell menu | ❓ | Phase 2 |
| Window thumbnails on hover | ✅ `ShowTaskThumbnails` | Check quality vs StartAllBack |
| Jump lists | ❓ | Phase 2 |
| Drag files onto task buttons / reorder buttons | 🟡 reorder (`SlideTaskbarButtons`) | Phase 2 |
| Centred task icons, Start on left | ❌ | Later |
| Segmented / translucent bar ("Aura", floating) | 🟡 `AllowBlurBehind` | Phase 4 |
| Auto-hide, incl. "when covered by a maximised window" | 🟡 plain auto-hide | Phase 2 |
| Multi-monitor taskbars | ✅ `ShowMultiMon`, `MultiMonMode` | — |
| Badges (unread counts) | ✅ `ShowTaskBadges` | — |
| Clock with seconds / custom format | ✅ | — |
| Volume on mouse wheel over tray icon | ✅ | — |
| Mic mute on middle-click | ❌ | Phase 2 |
| Network/battery/volume flyouts | ❓ opens Windows' own | Check in Phase 2 |

## Start menu (Open-Shell-Menu-Extreme)

| Feature | Stock | Plan |
|---|---|---|
| Classic one-click menus, cascading folders | ✅ | — |
| Fast search | ✅ | Check on 26H2 |
| Large icons in search/flyouts | ✅ configurable | — |
| Works with RetroBar's Start button | ❓ | Phase 2 |

## Explorer and system UI

| Feature | Stock | Plan |
|---|---|---|
| Ribbon / command bar choice | ❌ | Phase 3 |
| Details pane at bottom | ❌ | Phase 3 |
| Classic search box | ❌ | Phase 3 |
| Toolbar and status bar with sizes | ✅ Open-Shell ClassicExplorer | Check on 26H2 |
| Dark mode for more dialogs | ❌ | Phase 4 |
| Restyled context menus | ❌ | Phase 4 |
| Whole-window skins (WindowBlinds-style) | ❌ | Phase 4 module |
