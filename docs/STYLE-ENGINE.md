# Style engine — design pass

*12 Oct 2026 · status: **accepted in part**: Decision A decided (native sizing); B and slice order still open (❓)*

One part of RetroBar-Extreme that owns **how the taskbar looks**: sizes, text, fonts, icons and colours. All of it is driven by one saved *style* the owner can edit, and it works on top of any built-in theme.

## Why

Phase 1 kept finding problems that share a root cause:

| What we hit | Real cause |
|---|---|
| Jagged text at 105–150% (UX-002) | The whole taskbar is **stretched** by one scale factor; 100% pixels get smeared onto a non-matching grid |
| Native-size text looked like "a different font" | *Microsoft Sans Serif* is only hand-tuned near 11px |
| Orbitron only crisp at odd sizes; *Theme default* crisp everywhere at 100% | Orbitron has **no hinting** (no `fpgm` table): nothing snaps its strokes to pixels. MS Sans Serif is fully hinted |
| Weight choices don't work for Orbitron | Google's file is a **variable** font; WPF only sees its default weight and fakes bold |
| Bigger fonts overflowed the rows | Row height came from the theme, not from the text |
| Tray icons wrong colour on 26H2 | Inversion keyed to icon IDs and theme names, not to the actual background colour |
| Icons soft/jagged when scaled | Icons only come as 16px or 32px and are stretched to whatever the scale says |

Fixing each one separately means each fix fights the stretch. The owner's own finding points the other way: **at 100% everything is crisp.**

## Core idea: size things, don't stretch them

Instead of drawing at 100% and stretching, make every part the **right size at 100%**:

- **Text:** rendered at its real pixel size, in a font prepared for crisp rendering.
- **Icons:** drawn at a real icon size (16 / 20 / 24 / 32 px), never resampled.
- **Rows and buttons:** sized from text height + icon size + padding.
- **Lines and bevels:** stay exactly 1 or 2 px, which keeps the Win95 look sharp at any size.

This is how classic Windows itself handled bigger text: it changed sizes, it didn't zoom.

### ✅ Decision A — scaling model: **A1 native sizing is the default and target** *(owner, 12 Oct)*. Stretch stays as a selectable fallback; fancier stretch/scaling methods may be revisited much later.

| Option | What it means | Pros | Cons |
|---|---|---|---|
| **A1. Native sizing** *(recommended)* | *Taskbar scale* multiplies theme sizes (heights, widths, margins, font size) and picks real icon sizes; nothing is stretched | Crisp everything at any percentage, 1px lines stay 1px, no special text tricks needed | Themes hard-code some details (padding inside templates), so a few may look cramped or need small per-theme fixes; biggest single change |
| A2. Stretch + fix-ups *(current)* | Keep the stretch; counter-scale text (done), later icons | Already partly built; every theme works unchanged | Bevels and lines still blur at in-between scales; every new element needs its own fix-up |
| A3. Both, switchable | A1 as the new mode, A2 kept as "classic stretch" | Safe fallback per theme | Two code paths to keep working |

Implemented as UX-006 ([#9](https://github.com/techrote/RetroBar-Extreme/issues/9), [PR #10](https://github.com/techrote/RetroBar-Extreme/pull/10)): theme XAML is rescaled with whole-pixel rounding as it loads; borders and strokes are not scaled. The UX-002 counter-scale only runs in stretch mode.

## Fonts: a font pipeline

Crisp pixel text needs a font that is (1) a real static weight, (2) hinted, (3) used at a size it was designed or hinted for.

1. **Private fonts folder.** `Fonts\` beside RetroBar.exe (or in `%LOCALAPPDATA%`), loaded only by RetroBar: no system install, no conflicts.
2. **Prepared fonts.** For any OFL/open font the owner wants:
   - convert variable → one static file per weight;
   - auto-hint with *ttfautohint* (the same tool Google Fonts uses);
   - rename so it can't clash with the original.
   
   ✅ Probe done: **Orbitron Hinted** (ttfautohint) — owner: similar issues overall, nicer at their chosen size. Hinting helps but doesn't replace picking good sizes.
3. **A small curated set** of openly licensed pixel-style fonts designed for larger sizes, for the true Win9x look at 145%+. Licences checked per font before bundling.
4. **Size readout** keeps showing the real on-screen px (done in UX-005).

### ❓ Decision B — where fonts get prepared

| Option | Pros | Cons |
|---|---|---|
| **B1. Agent prepares packs on request** *(recommended for now)* | Zero code in RetroBar; owner just says "make me X"; already proven today | Owner depends on an agent session for new fonts |
| B2. Repo tool + CI: drop a font in a folder in UXUI-Extreme, GitHub builds the prepared pack | Repeatable, no agent needed | Some setup; still a download step |
| B3. RetroBar converts fonts itself at runtime | One-click for the owner | Bundling the hinting engine into a .NET app is real work and risk |

## Colours

From UX-003, with the theme-key map still the first job:

- Per-part **brush**: solid or linear gradient (stops + angle). Parts: bar, buttons (normal/hover/pressed/active), text, tray, clock, Start, borders.
- **Ratrod presets** as starting points, e.g. gunmetal, galvanised, oxide, matte black with one signal accent.
- **Derived rules** so things stay readable:
  - **tray icon inversion decided by background brightness** (replaces the theme-name rule and the 26H2 ID mismatch from UX-001);
  - warn on low text contrast.

## Styles: one saved thing

A **style** = base theme + overrides (geometry, font, colours, icon size). It is saved as a small file in `%LOCALAPPDATA%\RetroBar\Styles\`, switchable and exportable. The Properties **Style** tab (started in UX-005, finished in UX-004) edits the active style live. A broken style file never stops RetroBar starting: it logs and falls back to the plain theme.

## Slices (each one a normal issue → PR → owner test)

| # | Slice | Depends on | Notes |
|---|---|---|---|
| S1 | Font settings + row growth (**PR #8, UX-005**) | — | ✅ Merged, owner-tested |
| S2 | **Native sizing** (Decision A) — UX-006 | S1 | ✅ Merged, owner-tested. Owner will mostly run at **100% scale with larger fonts** |
| S3 | Real-size icons | S2 | Owner: icons already look fine after S2; low priority |
| S4 | Private fonts folder + first prepared/curated fonts | S1 | Pairs with Decision B |
| S5 | Theme-key map + colour layer (UX-003) | S2 | Map first, then brushes |
| S6 | Style files + editor (UX-004) | S5 | Turns settings into saved, switchable styles |
| S7 | Brightness-based tray inversion and contrast warnings | S5 | Closes UX-001's leftovers |

## Owner decisions needed

- ✅ **A — scaling model:** native sizing is default and target (owner, 12 Oct).
- ❓ **B — font preparation:** B1 now (agent-made packs), maybe B2 later?
- ❓ **Order:** S2 (native sizing) next, or S4 (fonts folder) first?
- Feedback wanted: plain **Orbitron** vs **Orbitron Hinted** at a few sizes.
