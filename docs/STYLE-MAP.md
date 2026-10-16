# Style map — which theme keys draw each taskbar part

*UX-003 ([issue](https://github.com/techrote/RetroBar-Extreme/issues/4), [PR #15](https://github.com/techrote/RetroBar-Extreme/pull/15)) · slice S5 of [STYLE-ENGINE.md](STYLE-ENGINE.md). Source of truth: `RetroBar/Utilities/StyleMap.cs`.*

The style layer (`%LOCALAPPDATA%\RetroBar\Style.json`) names **parts**. RetroBar's themes don't share resource names, so each part is mapped to the keys of the theme in use. Themes fall into three **families**, detected from the keys the theme defines:

| Family | Themes | Detected by |
|---|---|---|
| Classic | System, Windows 95-98, Me, 2000, XP Classic, Vista Classic | neither key below |
| Watercolor | Watercolor | `ButtonActiveBackground` |
| Modern | XP Blue, Olive Green, Silver, Royale, Royale Noir, Embedded, Zune · Vista Aero, Basic · Longhorn Aero | `TaskbarBackground` |

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

## Not mapped yet
- **Start button.** XP and Vista draw it as an image. Classic draws it with `ButtonFace`, so it follows `bar.background`.
- **Toolbar, tray toggle, scroll buttons, balloons and tooltips.** These keep the theme's look.
- **Tray icon inversion.** It still follows the base theme's `InvertSystemNotifyIcons`. Brightness-based inversion is slice S7.
- **Fonts.** These stay in the UX-005 settings.
