# StartAllBack parity checklist

A checklist of the owner's desired capabilities, not a fresh audit of the commercial product. **Checked 4 November 2026** against the fork snapshots in the [audit](audits/2026-11-04-quality-audit.md). ★ marks owner priorities.

The table now describes the **current fork**, because the old “Stock” column mixed upstream features with fork additions. “Present” means source/settings support was found; it does not mean owner-tested on the current build. Historical acceptance is linked in [PROGRAMME](PROGRAMME.md). Unchecked items require investigation rather than an assumed missing feature.

## Taskbar — RetroBar-Extreme

The implementation baseline is [`65b36c0`](https://github.com/techrote/RetroBar-Extreme/tree/65b36c0fba6ef8d8e44294b3ea332b03e32f638c), including its [feature inventory](https://github.com/techrote/RetroBar-Extreme/blob/65b36c0fba6ef8d8e44294b3ea332b03e32f638c/README.md) and [settings](https://github.com/techrote/RetroBar-Extreme/blob/65b36c0fba6ef8d8e44294b3ea332b03e32f638c/RetroBar/Utilities/Settings.cs).

| Capability | Current fork state | Remaining work / evidence boundary |
|---|---|---|
| ★ Window-title labels; never combine | Present: separate window buttons | Preserve the owner's never-combined setup; optional grouping is a future choice. |
| ★ Slim bar, small icons, adjustable dimensions | Scale/rows/width plus native sizing and UX-012–016 layout/button/icon controls are merged | Qualify the chosen geometry and mixed-DPI setup. |
| ★ Crisp scaled text | Native sizing default; stretch plus sharp-text option retained | UX-002 remains open; appearance depends on font, size, Windows DPI and rendering mode. |
| ★ Custom font family, size, weight, italic | UX-005 and separate clock controls implemented; UX-017 embeds 24 families | Arbitrary private-font-folder loading remains proposed; verify the actual selected face/weight. |
| ★ Colours and gradients | UX-003/004/009 implemented with editor, named styles and colourways | Mapping differs by theme family; see [STYLE-MAP](STYLE-MAP.md). |
| ★ Tray inversion responds to settings | UX-001 live set/clear implemented and historically accepted | Current code still uses per-icon/theme policy; background-brightness inversion remains S7. |
| Middle-click; Win+number | Present; historically owner-liked | Preserve behavior; do not confuse all possible click modifiers with the validated cases. |
| Top/left/right edges; multi-row/width | Present settings: `Edge`, `RowCount`, `TaskbarWidth` | Qualify combinations with custom layout and DPI. |
| Start button opens Open-Shell | Recognition/invocation/placement source exists | Exact module pair and target-Windows behavior unqualified; UX-020 first. |
| Hover thumbnails | `ShowTaskThumbnails` present | Quality versus owner's expectations needs a focused test. |
| Jump lists | Not qualified by this audit | Inspect implementation and current-Windows behavior before defining work. |
| File dragging / task-button reordering | Reordering setting `SlideTaskbarButtons` present | Delta also includes Quick Launch drop improvements; file-drop-to-running-application semantics remain unqualified. |
| Centred task icons with Start left | Per-row Centre alignment already exists in `TaskRowPanel`; the complete requested arrangement is not owner-qualified here | Test existing row alignment and Start placement together before proposing another centring feature. |
| Segmented/translucent/floating bar | Blur setting exists | Full floating/segmented design remains unqualified. |
| Auto-hide, including when covered by a maximised window | Basic auto-hide exists | Do not infer covered-window policy from the basic option. |
| Multiple monitors | `ShowMultiMon`, `MultiMonMode` present | Test exact monitors, DPI changes and recovery separately. |
| Badges; custom clock/seconds | Present; UX-008 added clock fit/spacing | Historical clock PASS is linked in the programme. |
| Volume wheel; system flyouts | Inherited paths/settings exist | Network/battery/volume behavior on current Windows remains to be checked. |
| Microphone mute by middle-click | Not qualified | Phase 2 investigation if selected. |
| Start recolouring | UX-010 implemented in a separate image pipeline | Not a brush part in `StyleMap`; protect source image/flag behavior. |
| LUT textures, angles and coherent patterns | UX-011/013 plus delta refinements implemented | Visual tiling/readability still depends on the selected style and scale. |
| PNG icons, tray-toggle image, per-app buttons | UX-014–016 merged | Persistence/fallback and exact layout require build-specific evidence. |
| Per-row app layout, alignment and height; Start/Quick and Icons controls | Delta implementation in PR #31/#33 | Preserve recorded scope; no per-feature current-build owner PASS inferred from release notes. |
| Complete style/configuration export | Style files export colour/texture/Start/border state | Theme/fonts/layout stay in settings; full configuration export remains proposed. |
| No automatic upstream updater | **Not met by inspected master** | [UX-019](https://github.com/techrote/RetroBar-Extreme/issues/34) repairs runtime and installer probes; older builds remain affected. |

## Start menu — Open-Shell-Menu-Extreme

Baseline: [`e1fe220`](https://github.com/techrote/Open-Shell-Menu-Extreme/tree/e1fe220d18bb38a0d8a19c70332d75fef4c2625f). Inherited capabilities are source-level only in this audit. No fork CI run, release or target-Windows owner acceptance was available.

| Capability | Source / qualification state | Next step |
|---|---|---|
| Classic menus, cascading folders, search and configurable icons | Inherited implementation exists | UX-020 build/VM gate, then qualify the desired menu settings on the recorded Windows build. |
| RetroBar Start-button pairing | RetroBar has a matching source path | Record both source SHAs, menu placement, Windows-key behavior and recovery. |
| No automatic updater; unsigned qualification | **Not met by inherited configuration** | [UX-020](https://github.com/techrote/Open-Shell-Menu-Extreme/issues/1): updater policy and non-publishing CI before testing. |
| Exit/uninstall restores stock behavior | Cleanup paths exist | Snapshot-VM test required; not established by code review. |

## Explorer and wider system UI

| Capability | Status | Programme |
|---|---|---|
| Explorer toolbar/status bar | Inherited ClassicExplorer source; current-Windows compatibility unqualified | Phase 3 after UX-020. |
| Ribbon/command-bar choice, bottom details pane, classic search box | No suite implementation qualified | Phase 3 investigation, each separately scoped. |
| Dark dialogs and restyled context menus | Planned | Phase 4. |
| Whole-window skins | No module selected | Phase 4; RetroBar theming does not supply this. |
