# Style engine — implementation and remaining design

The original design was recorded on 12 October 2026. **Reconciled 4 November 2026** against RetroBar [`65b36c0`](https://github.com/techrote/RetroBar-Extreme/tree/65b36c0fba6ef8d8e44294b3ea332b03e32f638c). Native sizing is implemented and the default. A single exported file containing every appearance setting remains a proposal.

## What is implemented

| Area | Current implementation | Source / task |
|---|---|---|
| Native sizing | Load theme dimensions at the requested taskbar scale; the native path uses a unit whole-bar transform. Stretch is selectable. | [ScaleModel](https://github.com/techrote/RetroBar-Extreme/blob/65b36c0fba6ef8d8e44294b3ea332b03e32f638c/RetroBar/Utilities/ScaleModel.cs), UX-006 |
| Text and layout | Taskbar/clock font controls, row adjustment, line spacing, clock orientation and button layout are implemented. | UX-005/007/008/012/014 in [PROGRAMME](PROGRAMME.md) |
| Fonts | 24 families embedded as WPF resources; installed fonts also selectable. Knurled Swarf has size-specific faces. | [BundledFonts](https://github.com/techrote/RetroBar-Extreme/blob/65b36c0fba6ef8d8e44294b3ea332b03e32f638c/RetroBar/Utilities/BundledFonts.cs), UX-017 |
| Custom icons | PNG overrides and size sets for Start/quick-launch; tray-toggle customization. Selection/scaling depends on available source sizes. | UX-015/016, [PR #24](https://github.com/techrote/RetroBar-Extreme/pull/24) |
| Colour layer | Per-part solid/gradient/texture overrides, generated colourways, named styles, a 12-slot colour palette and 20-slot texture palette. | [StyleDocument](https://github.com/techrote/RetroBar-Extreme/blob/65b36c0fba6ef8d8e44294b3ea332b03e32f638c/RetroBar/Utilities/StyleDocument.cs), [STYLE-MAP](STYLE-MAP.md) |
| Start and borders | Separate `start.recolour` image treatment and `borders` factors; current border range is integer 0–16, not the original issue's 0–4. | [Start document](https://github.com/techrote/RetroBar-Extreme/blob/65b36c0fba6ef8d8e44294b3ea332b03e32f638c/RetroBar/Utilities/StyleDocument.Start.cs), [border document](https://github.com/techrote/RetroBar-Extreme/blob/65b36c0fba6ef8d8e44294b3ea332b03e32f638c/RetroBar/Utilities/StyleDocument.Borders.cs) |

These are source facts. Historical visual acceptance and current CI evidence are recorded separately in [the audit](audits/2026-11-04-quality-audit.md).

## Native sizing and Windows DPI

**Decision A is resolved:** native sizing is the default and target, with stretch retained as a fallback. UX-006 already implemented the choice; there is no pending “S2 or fonts first?” decision.

| Mode | Theme sizes | Whole-taskbar transform |
|---|---|---|
| Native | Scaled as the theme loads | 1 on the native scaled path |
| Stretch | Theme loaded at its base size | `TaskbarScale` |

At 100% taskbar scale both paths use unit scaling. The sharp-text counter-scaling belongs to the stretch path. Theme geometry, text and icon helpers need to agree on the selected mode; new code should use the existing helpers rather than apply a second scale.

WPF uses device-independent units which scale with Windows DPI. Rounding a theme dimension to a whole layout unit is not a guarantee of a one-physical-pixel line at every monitor scale. Fonts and bitmap sources can still require rasterization or resampling. Native sizing removes the unnecessary whole-taskbar stretch, but does not guarantee crispness for every font/image/size. See [Microsoft's WPF layout and rounding explanation](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/advanced/layout#sub-pixel-rendering-and-layout-rounding).

Borders are treated separately from overall theme scaling and can be explicitly overridden. Preserve that distinction when adding dimensions; do not infer that every border is always exactly 1 physical pixel.

## Fonts: established observations and future options

The owner's October comparisons found size-dependent results with the tested Orbitron and Orbitron Hinted files, and preferred the hinted variant at the chosen size. Keep that as a dated observation. The old diagnosis “no `fpgm` table means no hinting” was too strong: OpenType's [`fpgm` table is optional](https://learn.microsoft.com/en-us/typography/opentype/spec/fpgm), and [`glyf` can contain per-glyph instructions](https://learn.microsoft.com/en-us/typography/opentype/spec/glyf). Identify the actual font file and inspect its relevant tables before diagnosing its hinting or weight behavior.

The current bundled-font implementation supersedes part of the original “first curated fonts” proposal. A generic private `Fonts\` directory loader, automatic variable-font conversion and runtime auto-hinting are **not established shipped features**. Any new prepared font pack must retain its license, distinguish static faces/weights correctly, and be tested at the requested sizes. The filename or family name alone is not evidence of rendering quality.

The old Decision B remains a choice only if additional preparation is wanted:

| Option | Use | Tradeoff |
|---|---|---|
| Agent prepares a requested pack | Small number of selected fonts | Low application complexity; requires a preparation task. |
| Repeatable repository/CI preparation tool | Repeated pack generation | Reproducible inputs and licensing record; additional maintenance. |
| Runtime preparation inside RetroBar | Only if explicitly selected later | More native dependencies and failure paths; not part of current behavior. |

## What a saved style contains

The active colour/style layer is `%LOCALAPPDATA%\RetroBar\Style.json`; named copies live in `Styles\`. Application settings remain in `%LOCALAPPDATA%\RetroBar\settings.json`. Portable builds use the same directory.

| Stored in a style | Stored separately / not a complete style export |
|---|---|
| Per-part brushes, gradients and textures | Base theme selection |
| Colour and texture palettes | Taskbar and clock font settings |
| Start recolouring | Layout, scale, row/clock/button settings |
| Per-part border factors | Custom image files and other application settings |

Saving a named style therefore does not back up the whole taskbar configuration. Keep settings and referenced user assets when making a full backup. Applying a colourway already writes the active style; saving a named copy is optional, as clarified in the [UX-009 acceptance record](https://github.com/techrote/RetroBar-Extreme/issues/17#issuecomment-6219971124).

A unified style/configuration bundle remains a future design. It needs a versioned schema, explicit migration rules, asset handling and failure/recovery tests before it can replace the split storage. The existing style reader skips invalid values and the layer has fallback handling; this audit reviewed those paths but did not run a new Windows startup test.

## Colours and remaining rules

The [theme-key map](STYLE-MAP.md) controls brushes for bar, tray, button states, text, clock and bevels. Start image recolouring is a separate pipeline. Per-part border factors are also separate from the brush map.

**S7 remains open design:** background-brightness tray inversion and general low-contrast warnings are not implemented as universal rules. The current tray path still combines mode, per-icon selection and the base theme's inversion flag. Generated colourways contain limited foreground contrast selection; that is not a warning system for every arbitrary gradient, texture or user override. New work needs a defined luminance/contrast policy and owner comparison before changing defaults.

## Original slice reconciliation

| Slice | Disposition at the inspected source |
|---|---|
| S1 — fonts and row growth | UX-005 merged; historical owner report linked in the programme. |
| S2 — native sizing | UX-006 merged and adopted; no longer a sequencing question. |
| S3 — real-size icons | UX-015 adds custom size sets; available assets and scaling fallback still matter. Do not promise all icons are never resampled. |
| S4 — private/prepared fonts | UX-017 embeds 24 families; generic private-directory loading and preparation automation remain proposals. |
| S5 — map and colour layer | UX-003 merged; [STYLE-MAP](STYLE-MAP.md) describes the current mapping. |
| S6 — style files and editor | UX-004 merged for colour/style state; not a unified settings bundle. |
| S7 — brightness/contrast policy | Still proposed; UX-001's deferred default matching remains relevant. |

Next work should be selected from the remaining gaps after checking live module issues, rather than treating this historical slice list as an unimplemented feature backlog.
