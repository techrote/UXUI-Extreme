# RAG — UXUI-Extreme

Compact, authoritative context. If an issue conflicts with this file, reconcile against live repo state and record the newer decision here.

## Goal

Replace StartAllBack on the owner's machines with a suite we control, then go beyond it. Personal use only.

## Target system

- Windows 11 **26H2, build 26300.9457** (owner's daily machine, October 2026). Expect later builds; don't hard-code build numbers into behaviour.
- Owner's machines: 5600X/Titan RTX + V100, 2600X/K80, E5-2686 v4/RTX 4000, i7-6700/Quadro M620.

## What the owner wants

- **Taskbar (from their StartAllBack setup):** slim, consistent and informative. Small icons, labelled window buttons showing titles, never-combined, pinned shortcuts, compact tray, clock.
- **Daily setup (12 Oct):** 100% taskbar scale; *Orbitron Hinted* 17px weight 600; *Row height adjust* −4 (no padding wanted under the lower row). *Theme default* (hinted MS Sans Serif) looks right at all sizes and weights; unhinted fonts such as Orbitron only look crisp at some sizes, which is a property of the font.
- **Already liked in stock RetroBar:** middle-click on task buttons, Win+number shortcuts.
- **Look:** industrial, down-to-earth, non-neon "ratrod" cyberpunk. Function over form, but it should look tough rather than glossy. Pixel-style "system" fonts are welcome; blurry smoothing is not.

## Decisions

- **D-001 — Taskbar by replacement, not Explorer hooks.** Windows 24H2+ removed the old taskbar code from Explorer. StartAllBack and ExplorerPatcher ship their own reimplementations injected into Explorer, which breaks on updates and trips antivirus. We use a separate replacement taskbar (RetroBar) instead: it survives updates and quitting it restores Windows' own taskbar. *(12 Oct 2026)*
- **D-002 — Modular forks, one umbrella.** Each module is a fork of an existing open-source project; this repo holds plan, checklist and issues. Forks keep upstream mergeability. *(12 Oct 2026)*
- **D-003 — Personal-use focus.** No signing or store distribution work is planned. The forks have **public releases and downloads**; preserve upstream notices/licences and obey applicable licence conditions, especially when redistributing binaries or bundled fonts. The old statement that licences only matter on redistribution was too broad. *(12 Oct decision; clarified 4 Nov 2026)*
- **D-005 — Native sizing over stretching.** At any taskbar scale, draw everything at its real size (theme sizes rescaled with whole-pixel rounding, real text sizes, borders kept 1px) rather than drawing at 100% and stretching. Stretch remains a fallback mode. See [docs/STYLE-ENGINE.md](docs/STYLE-ENGINE.md). *(12 Oct 2026)*
- **D-004 — No reverse engineering of commercial products** (StartAllBack, WindowBlinds). Use open-source references and Microsoft documentation. *(12 Oct 2026)*

## RetroBar-Extreme facts

- C#/WPF; the October 2026 implementation targets `net6.0-windows` and `net10.0-windows`. Tray and task-list plumbing comes from the **ManagedShell** NuGet package. The old ~9k-line estimate predates multiple feature additions and should not be used for current sizing.
- CI: `.github/workflows/retrobar.yml` builds installers and **portable zips** on push/PR to `master` (windows-2025 runners). Portable zips are how the owner tests.
- **Themes** are XAML resource dictionaries in `RetroBar/Themes/`. `System.xaml` is always loaded first; the chosen theme is merged on top. Custom themes load from `%LOCALAPPDATA%\RetroBar\Themes\` or a `Themes` folder beside the exe (`Utilities/DictionaryManager.cs`). Active colour overrides use `%LOCALAPPDATA%\RetroBar\Style.json`; named styles are kept separately under `Styles\`.
- **Settings** live in `Utilities/Settings.cs` (one property per option, change notifications drive the UI).
- **Scaling:** historical upstream behaviour uses `LayoutTransform` stretching; the fork's UX-006 implementation uses **native sizing by default** and retains stretch as a fallback. The UX-002 sharp-text counter-scale is relevant to stretch mode, not an accurate description of the default. Windows DPI still matters.
- **Tray icon inversion:** `Controls/NotifyIcon.xaml.cs` `applyEffects()` applies `InvertEffect` (a pixel shader) per icon. Inputs: `Settings.InvertIconsMode`, the per-icon list `Settings.InvertNotifyIcons`, and the theme resource `InvertSystemNotifyIcons`.

## Source-qualified programme baseline (4 November 2026)

- RetroBar-Extreme `master`: [65b36c0](https://github.com/techrote/RetroBar-Extreme/commit/65b36c0fba6ef8d8e44294b3ea332b03e32f638c) (18 October). The latest inspected build, [workflow run 39116769177](https://github.com/techrote/RetroBar-Extreme/actions/runs/39116769177), completed successfully on this commit; separate Extras, Start-colourways and LUT-texture contract workflows also passed.
- Latest verified published release: [v1.23.43-extreme-delta.1](https://github.com/techrote/RetroBar-Extreme/releases/tag/v1.23.43-extreme-delta.1), 18 October 2026. Its notes report owner-tested daily use; this is not a separate feature-by-feature Windows acceptance record.
- UX-012–016 landed together in [PR #24](https://github.com/techrote/RetroBar-Extreme/pull/24), merged 17 October; UX-017 landed in [PR #30](https://github.com/techrote/RetroBar-Extreme/pull/30). Subsequent delta polish landed in #31/#33.
- The fork now has built-in fonts, saved example styles, an Icons/Start-Quick UI, extra patterns, row layout, and per-app task-button overrides. See [the current programme](docs/PROGRAMME.md) and [parity checklist](docs/PARITY.md) rather than interpreting older feature proposals as missing implementations.
- Outstanding: cross-application Start-menu interoperability, jump lists, niche auto-hide modes, and broader Windows visual/safety qualification are **not** established by the documentation-only audit.
- All statements above are snapshots: refresh current GitHub branches, PRs and CI before an integration decision.

## Open-Shell-Menu-Extreme facts

- C++ (ATL/Win32), Visual Studio 2022 solution `Src/OpenShell.sln`. CI: `.github/workflows/build.yml` on PRs to `master`.
- Taskbar support is limited to recolouring/texturing the existing Windows taskbar; it cannot add labels, ungrouping or a classic tray.
