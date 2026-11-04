# Style map — which theme keys draw each taskbar part

*UX-003 ([issue](https://github.com/techrote/RetroBar-Extreme/issues/4), [PR #15](https://github.com/techrote/RetroBar-Extreme/pull/15)) · slice S5 of [STYLE-ENGINE.md](STYLE-ENGINE.md). Checked 4 November 2026 against [StyleMap.cs at `65b36c0`](https://github.com/techrote/RetroBar-Extreme/blob/65b36c0fba6ef8d8e44294b3ea332b03e32f638c/RetroBar/Utilities/StyleMap.cs), the implementation authority for this table.*

The style layer (`%LOCALAPPDATA%\RetroBar\Style.json`) names **parts**. RetroBar's themes don't share resource names, so each part is mapped to the keys of the theme in use. Themes fall into three **families**, detected from the keys the theme defines:

| Family | Themes | Detected by |
|---|---|---|
| Classic | System, Windows 95-98, Me, 2000, XP Classic, Vista Classic | neither key below |
| Watercolor | Watercolor | `ButtonActiveBackground` |
| Modern | XP Blue, Olive Green, Silver, Royale, Royale Noir, Embedded, Zune · Vista Aero, Basic · Longhorn Aero | `TaskbarBackground` |

Detection checks `TaskbarBackground` first, then `ButtonActiveBackground`, then falls back to Classic. If a custom theme has both keys, Modern wins. This is resource-family detection, not a guarantee that every custom template uses every mapped key.

Key roles:

- **fill** gets the part's brush.
- **fill ⟂** gets the brush turned 90°, for a vertical taskbar.
- **clear** is set to transparent. These are theme overlays that would tint a custom background.

On Modern themes a key is set only if the theme defines it.

## Classic

| Part.property | Keys | Notes |
|---|---|---|
| bar.background | `ButtonFace` | Also the tray, Start button and (unless `button.background` is set) task buttons: classic draws them all with one colour |
| button.background | *copy of the theme's `TaskButton` style, Background setter* | Classic buttons use `ButtonFace` through the style's Background |
| buttonActive.background | `CheckeredBackground` | Replaces the dither pattern |
| buttonFlashing.background | `ButtonFlashingFace` | |
| button.foreground | `ButtonForeground` | Also active buttons |
| buttonFlashing.foreground | `ButtonFlashingForeground` | |
| clock.foreground | `ClockForeground` | |
| bevel.highlight / light / shadow / darkShadow | `ButtonHighlight` + `ButtonInnerHighlight` / `ButtonLight` / `ButtonShadow` / `ButtonDarkShadow` | The 3D edges of everything |
| *not mapped* | tray, button border, hover | Classic has no separate tray colour, button border or hover state |

## Watercolor

| Part.property | Keys |
|---|---|
| bar.background / border | `ButtonFace` / `ButtonBorder` |
| tray.background / border | `TrayBackground` / `TrayBorder`, `TrayInnerBorder` |
| button.background / border | *`TaskButton` style copy* / `ButtonInactiveBorder` |
| buttonHover.background / border | `ButtonHoverBackground` / `ButtonHoverBorder` |
| buttonActive.background / border | `ButtonActiveBackground`, `ButtonPressedBackground` / `ButtonActiveBorder`, `ButtonPressedBorder` |
| buttonFlashing.background / border | `ButtonFlashingBackground` / `ButtonFlashingBorder` |
| button / buttonActive .foreground | `ButtonForeground` / `ButtonPressedForeground` |
| clock.foreground | `ClockForeground` |
| bevel.highlight / shadow | `ButtonLight` / `ButtonShadow` |

## Modern (XP, Vista, Longhorn)

| Part.property | fill | fill ⟂ | clear |
|---|---|---|---|
| bar.background | `TaskbarBackground`, `TaskbarBackgroundTall`, `TaskbarWindowBackground` | `TaskbarVerticalBackground` | `TaskbarBackgroundGlow`, `TaskbarVerticalBackgroundGlow` |
| bar.border | `TaskbarBorder`, `TaskbarTopBorder`, `TaskbarBottomBorder`, `TaskbarVerticalTopBorder`, `TaskbarVerticalBottomBorder`, `TaskbarUnlockedBorderTop` | | |
| tray.background | `TrayBackground` | `TrayVerticalBackground` | |
| tray.border | `TrayTopBottomBorder`, `TrayTopBorder`, `TrayBottomBorder`, `TrayOuterBorderVertical`, `TrayLeftBorder1` | | `TrayLeftBorder4` |
| button*.background | `TaskButtonBackground{s}` | | `TaskButtonBackgroundHighlight{s}`, `TaskButtonBottomBackground{s}` |
| button*.border | `TaskButton{Top,Left,Right,Bottom,Outer,BottomRight}Border{s}` | | |
| button.foreground | `ButtonForeground` | | |
| buttonActive.foreground | `ButtonActiveForeground`, `ButtonPressedForeground` | | |
| buttonFlashing.foreground | `ButtonFlashingForeground` | | |
| clock.foreground | `ClockForeground` | | |
| bevel.highlight | bar inner borders (`TaskbarTopInnerBorder`, `…1/2`, `TaskbarBottomInnerBorder`, vertical variants), `TrayLeftBorder2/3`, button inner light edges (`TaskButtonInner{Left,,TopRight,BottomLeft,Vertical,Horizontal,Top}Border{s}`) | | |
| bevel.shadow | button inner dark edges (`TaskButtonInner{Right,Bottom}Border{s}`) | | |

State suffix `{s}`:

| Part | `{s}` |
|---|---|
| button | none |
| buttonHover | `Hover` |
| buttonActive | `Pressed`, `PressedHover` (XP); `Active`, `ActiveHover` (Vista, Longhorn) |
| buttonFlashing | `Flashing` |

On pushed-in (active) buttons the inner bevel is swapped: the light edges take `bevel.shadow` and the dark edges take `bevel.highlight`.

## Outside this brush map

- **Start image recolouring is implemented separately.** UX-010's top-level `start.recolour` uses the image pipeline; it is not a `start.background` brush part. Classic follows `ButtonFace`/`bar.background`. UX-015 also supports a custom Start icon. [Start document source](https://github.com/techrote/RetroBar-Extreme/blob/65b36c0fba6ef8d8e44294b3ea332b03e32f638c/RetroBar/Utilities/StyleDocument.Start.cs).
- **Border thickness is separate from border colour.** Top-level `borders` supports `bar`, `tray`, `button`, `buttonActive`, `buttonFlashing`, `clock` and `start`, with whole-number factors 0–16 at the inspected source. It is applied during theme loading, rather than by the brush-key mapping. [Border source](https://github.com/techrote/RetroBar-Extreme/blob/65b36c0fba6ef8d8e44294b3ea332b03e32f638c/RetroBar/Utilities/StyleDocument.Borders.cs).
- **Toolbar, scroll buttons, balloons and tooltips** have no independent per-part brush mapping here. Some shared theme resources can affect more than one component. The tray-toggle image/margins are separately customizable through UX-016.
- **Tray icon inversion** still combines mode, per-icon selection and the base theme's `InvertSystemNotifyIcons`; background-brightness inversion remains proposed S7. Custom replacement tray images have their own path.
- **Fonts and layout** remain application settings, not fields in this brush map or a complete exported style bundle. See [STYLE-ENGINE](STYLE-ENGINE.md).
