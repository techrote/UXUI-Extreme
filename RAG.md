# RAG — UXUI-Extreme

Compact, authoritative context. If an issue conflicts with this file, reconcile against live repo state and record the newer decision here.

## Goal

Replace StartAllBack on the owner's machines with a suite we control, then go beyond it. Personal use only.

## Target system

- Windows 11 **26H2, build 26300.9457** (owner's daily machine, October 2026). Expect later builds; don't hard-code build numbers into behaviour.
- Owner's machines: 5600X/Titan RTX + V100, 2600X/K80, E5-2686 v4/RTX 4000, i7-6700/Quadro M620.

## What the owner wants

- **Taskbar (from their StartAllBack setup):** slim, consistent and informative. Small icons, labelled window buttons showing titles, never-combined, pinned shortcuts, compact tray, clock.
- **Already liked in stock RetroBar:** middle-click on task buttons, Win+number shortcuts.
- **Look:** industrial, down-to-earth, non-neon "ratrod" cyberpunk. Function over form, but it should look tough rather than glossy. Pixel-style "system" fonts are welcome; blurry smoothing is not.

## Decisions

- **D-001 — Taskbar by replacement, not Explorer hooks.** Windows 24H2+ removed the old taskbar code from Explorer. StartAllBack and ExplorerPatcher ship their own reimplementations injected into Explorer, which breaks on updates and trips antivirus. We use a separate replacement taskbar (RetroBar) instead: it survives updates and quitting it restores Windows' own taskbar. *(12 Oct 2026)*
- **D-002 — Modular forks, one umbrella.** Each module is a fork of an existing open-source project; this repo holds plan, checklist and issues. Forks keep upstream mergeability. *(12 Oct 2026)*
- **D-003 — Personal use.** No signing, packaging or distribution work. Licences only matter if something is redistributed; keep each fork under its upstream licence. *(12 Oct 2026)*
- **D-004 — No reverse engineering of commercial products** (StartAllBack, WindowBlinds). Use open-source references and Microsoft documentation. *(12 Oct 2026)*

## RetroBar-Extreme facts

- C#/WPF, ~9k lines. Targets `net6.0-windows` and `net10.0-windows`. Tray and task-list plumbing comes from the **ManagedShell** NuGet package.
- CI: `.github/workflows/retrobar.yml` builds installers and **portable zips** on push/PR to `master` (windows-2025 runners). Portable zips are how the owner tests.
- **Themes** are XAML resource dictionaries in `RetroBar/Themes/`. `System.xaml` is always loaded first; the chosen theme is merged on top. Custom themes load from `%LOCALAPPDATA%\RetroBar\Themes\` or a `Themes` folder beside the exe (`Utilities/DictionaryManager.cs`).
- **Settings** live in `Utilities/Settings.cs` (one property per option, change notifications drive the UI).
- **Scaling:** the whole taskbar is scaled with a `LayoutTransform` (`TaskbarScale`) on top of Windows' DPI scaling. Text mode is chosen by `SettingsToTextFormattingModeConverter` (Display unless scaled with smoothing on) and `BoolToTextRenderingModeConverter` (Aliased when smoothing off).
- **Tray icon inversion:** `Controls/NotifyIcon.xaml.cs` `applyEffects()` applies `InvertEffect` (a pixel shader) per icon. Inputs: `Settings.InvertIconsMode`, the per-icon list `Settings.InvertNotifyIcons`, and the theme resource `InvertSystemNotifyIcons`.

## Open-Shell-Menu-Extreme facts

- C++ (ATL/Win32), Visual Studio 2022 solution `Src/OpenShell.sln`. CI: `.github/workflows/build.yml` on PRs to `master`.
- Taskbar support is limited to recolouring/texturing the existing Windows taskbar; it cannot add labels, ungrouping or a classic tray.
