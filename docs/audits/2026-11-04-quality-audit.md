# UX-018 — repository quality audit and corrections

**Checked:** 4 November 2026. **Owning issue:** [UXUI-Extreme #5](https://github.com/techrote/UXUI-Extreme/issues/5). **Umbrella baseline:** [`59d6b2f13a608151d21456514f3fb0ff6522ce5f`](https://github.com/techrote/UXUI-Extreme/commit/59d6b2f13a608151d21456514f3fb0ff6522ce5f).

The baseline contained seven Markdown files, no application implementation, no tests and no Actions runs. Its main defect was stale or overconfident guidance for the two module forks. All 14 existing relative Markdown links resolved; broken local links were not an audit finding. The new navigation checker prevents future link/anchor regressions rather than repairing a fictitious existing one.

## Scope and evidence method

Reviewed every umbrella document and compared its claims with exact module source, issues/comments, PR merge metadata, workflow runs, artifacts and release/tag metadata. Independent reviewers examined RetroBar state, Open-Shell state and internal documentation consistency. The code-based checks added here are offline and do not establish live GitHub state or Windows behavior.

| Repository | Default branch | Inspected commit | Evidence available at the initial snapshot |
|---|---|---|---|
| UXUI-Extreme | `main` | `59d6b2f13a608151d21456514f3fb0ff6522ce5f` | Seven documents; no Actions runs; old umbrella UX-001–004 issues closed. |
| RetroBar-Extreme | `master` | [`65b36c0fba6ef8d8e44294b3ea332b03e32f638c`](https://github.com/techrote/RetroBar-Extreme/commit/65b36c0fba6ef8d8e44294b3ea332b03e32f638c) | Build and three contract workflows successful. No open PR; UX-002 #3 the only open issue before this audit created UX-019. |
| Open-Shell-Menu-Extreme | `master` | [`e1fe220d18bb38a0d8a19c70332d75fef4c2625f`](https://github.com/techrote/Open-Shell-Menu-Extreme/commit/e1fe220d18bb38a0d8a19c70332d75fef4c2625f) | No fork Actions runs or releases returned; issue/PR collections initially empty before UX-020 was created. Source review only. |

These are dated observations, not an assertion that a repository never had older activity or that no later work exists. Full heads, rather than mutable branch links, identify the inspected implementation.

## Concurrent audit integration

While this audit was being published, [PR #7](https://github.com/techrote/UXUI-Extreme/pull/7) merged a parallel UX-018 documentation pass as `6f679dc0dfe0a162fc04c299054c2c58e3729e9f`, closing [issue #6](https://github.com/techrote/UXUI-Extreme/issues/6). [PR #8](https://github.com/techrote/UXUI-Extreme/pull/8), owned by earlier issue #5, reconciles against that main rather than replacing its history. The repeated UX-018 label came from concurrent allocation; it is recorded here instead of renumbering completed work.

The [earlier audit](../AUDIT-2026-11-04.md), release chronology, delta layout/icon scope, legacy-issue routing and four original checker regressions are retained. Its mistaken “five Markdown files” count is annotated. The new checker provides one shared implementation in `tools/check_docs.py`; the existing `scripts/check_docs.py` entry point/API delegates to it. There is one documentation workflow at `.github/workflows/docs-quality.yml`, strengthened with pinned checkout, exact-head selection, non-persisted credentials and superseded-run cancellation. The duplicate workflow is removed, so this integration does not double CI work.

The reconciled suite has 19 tests: 14 navigation regressions, the four preserved tests, and a subprocess test of the public entry point from a different working directory. Independent review and final-head CI are repeated after the merge resolution.

## Findings and implemented umbrella fixes

| Priority | Finding in the baseline | Correction / disposition |
|---|---|---|
| High | README claimed every module PR supplied a `portable` ZIP that needed no installation. | Split module instructions. RetroBar needs a matching Desktop Runtime; Open-Shell's inherited outputs are installer/symbols/utility. Added [BUILD-AND-TEST](../BUILD-AND-TEST.md) with direct, source-bound links and artifact-expiry limits. |
| High | Portable packaging was liable to be mistaken for isolated settings. | Documented shared `%LOCALAPPDATA%\RetroBar` storage and the distinction between a style export and full settings/assets backup. |
| High | Suite “no updaters calling home” policy was presented without acknowledging inherited updater paths. | Retained the requirement and recorded the actual gaps. A bounded RetroBar runtime/installer repair is owned by [UX-019](https://github.com/techrote/RetroBar-Extreme/issues/34); Open-Shell prerequisite work is [UX-020](https://github.com/techrote/Open-Shell-Menu-Extreme/issues/1). Neither is silently treated as accepted on the inspected default branches. |
| High | Open-Shell manual dispatch was liable to be treated as a harmless build-only route. | Documented its SignPath and prerelease/tag steps and prevented that interpretation in AGENTS, RAG, programme and build guidance. No inherited workflow was dispatched. |
| Medium | UX-012–014 still said “in PR”; UX-015–017 and later delta work were absent. | Reconciled [PROGRAMME](../PROGRAMME.md) with merged PRs #24/#30/#31/#33 and restored all task ownership links. UX-002 remains open. |
| Medium | “Stock” parity mixed upstream capabilities with fork additions and described shipped fonts/colours as future work. | Rebuilt [PARITY](../PARITY.md) around the inspected fork and separate remaining qualification, without claiming a fresh upstream or commercial-product audit. |
| Medium | RAG universally described whole-bar stretch; design still asked whether already-merged S2 should happen next. | Recorded native default versus stretch fallback and removed obsolete sequencing decisions. |
| Medium | Unified style export, generic private-font loading, background-based inversion and contrast warnings were narrated as shipped. | Separated implemented storage/embedded fonts from remaining proposals. Added actual Start image and border paths outside the brush map. |
| Medium | Missing `fpgm` was treated as proof of no hinting; whole-number WPF layout was equated with physical pixels. | Narrowed the historical font report and cited Microsoft's OpenType and WPF specifications. Native sizing is a rendering approach, not a universal crispness guarantee. |
| Medium | Owner-tested labels lacked evidence boundaries; “agent-tested” was undefined. | Linked historical reports and preserved exactness limits. Defined source review, compilation, named automated checks and owner-tested as distinct evidence. |
| Medium | Guidance implied guaranteed Windows-update resilience, blanket license exemptions and no published packages. | Preserved the separate-process/personal-use decisions while removing unsupported guarantees; require retained licenses/attribution and acknowledge existing personal prereleases. |
| Medium | Agent routing always said “issue in this repo” and required `//` comments even for other source languages. | Route to the actual owning repository; use source-language comments only where appropriate. Preserve historical grouped PR #24 without rewriting its history. |
| Preventive | No automated documentation validation existed. | Added a dependency-free local link/anchor checker, regression fixtures and one read-only, bounded GitHub Actions job. It does not claim to detect live factual drift. |

The priority labels describe impact on build selection, development decisions and evidence quality. They are not a security-severity certification of the Windows applications.

## RetroBar source, builds and release provenance

The following runs all report `head_sha = 65b36c0fba6ef8d8e44294b3ea332b03e32f638c`, event `push`, conclusion `success`:

| Workflow | Run |
|---|---|
| RetroBar build/package | [39116769177](https://github.com/techrote/RetroBar-Extreme/actions/runs/39116769177) |
| Start colourways contracts | [39116769188](https://github.com/techrote/RetroBar-Extreme/actions/runs/39116769188) |
| LUT texture contracts | [39116769180](https://github.com/techrote/RetroBar-Extreme/actions/runs/39116769180) |
| Extras contracts | [39116769196](https://github.com/techrote/RetroBar-Extreme/actions/runs/39116769196) |

Artifacts `12132522901` (**RetroBar Portable 64-bit**) and `12132687761` (**RetroBar Portable**) were unexpired, with expiry recorded as 16 January 2027. Exact links and prerequisites are in [BUILD-AND-TEST](../BUILD-AND-TEST.md). The normal portable profile is framework-dependent; the workflow selects .NET 10 for Windows 11 and separately labels the .NET 6 Win7-8 artifacts.

The newest observed [prerelease](https://github.com/techrote/RetroBar-Extreme/releases/tag/v1.23.43-extreme-delta.1) was published 18 October 2026 and its tag resolved to the inspected commit. The releases/latest API returned 404; the audit used the release collection and exact tag so that prereleases were not overlooked. Release metadata does not itself prove byte-level equivalence to the CI artifact or constitute a new owner test.

Key source references:

| Claim | Immutable implementation reference |
|---|---|
| Build matrix, events and artifact names | [retrobar.yml](https://github.com/techrote/RetroBar-Extreme/blob/65b36c0fba6ef8d8e44294b3ea332b03e32f638c/.github/workflows/retrobar.yml) |
| Framework-dependent x64 portable profile | [x64-portable.pubxml](https://github.com/techrote/RetroBar-Extreme/blob/65b36c0fba6ef8d8e44294b3ea332b03e32f638c/RetroBar/Properties/PublishProfiles/x64-portable.pubxml) |
| Native/stretch path | [ScaleModel.cs](https://github.com/techrote/RetroBar-Extreme/blob/65b36c0fba6ef8d8e44294b3ea332b03e32f638c/RetroBar/Utilities/ScaleModel.cs) |
| Shared saved-data location | [ManagementExtensions.cs](https://github.com/techrote/RetroBar-Extreme/blob/65b36c0fba6ef8d8e44294b3ea332b03e32f638c/RetroBar/Extensions/ManagementExtensions.cs) |
| Style fields and palettes | [StyleDocument.cs](https://github.com/techrote/RetroBar-Extreme/blob/65b36c0fba6ef8d8e44294b3ea332b03e32f638c/RetroBar/Utilities/StyleDocument.cs), [Start](https://github.com/techrote/RetroBar-Extreme/blob/65b36c0fba6ef8d8e44294b3ea332b03e32f638c/RetroBar/Utilities/StyleDocument.Start.cs), [borders](https://github.com/techrote/RetroBar-Extreme/blob/65b36c0fba6ef8d8e44294b3ea332b03e32f638c/RetroBar/Utilities/StyleDocument.Borders.cs) |
| 24 bundled font families | [BundledFonts.cs](https://github.com/techrote/RetroBar-Extreme/blob/65b36c0fba6ef8d8e44294b3ea332b03e32f638c/RetroBar/Utilities/BundledFonts.cs) |
| Original automatic update paths | [Updater.cs](https://github.com/techrote/RetroBar-Extreme/blob/65b36c0fba6ef8d8e44294b3ea332b03e32f638c/RetroBar/Utilities/Updater.cs), [installer.iss](https://github.com/techrote/RetroBar-Extreme/blob/65b36c0fba6ef8d8e44294b3ea332b03e32f638c/installer.iss) |
| Open-Shell recognition and placement | [StartMenuMonitor.cs](https://github.com/techrote/RetroBar-Extreme/blob/65b36c0fba6ef8d8e44294b3ea332b03e32f638c/RetroBar/Utilities/StartMenuMonitor.cs) |

## Historical owner acceptance records

The following are **recorded issue reports**, several posted as generated summaries under the owner's GitHub account. They are retained as historical evidence; this audit did not reproduce the tests or reconstruct an unseen original conversation. Short-SHA or PR-only records are not silently upgraded to full artifact custody.

| Work | Record | Exactness / limitation |
|---|---|---|
| UX-001 | [12 October PASS](https://github.com/techrote/RetroBar-Extreme/issues/2#issuecomment-6124231926) | Names PR #1 build and Windows version; records merge `05147c5`. Also corrects the original diagnosis: default matching missed the white tray icons. |
| UX-005 | [Font report](https://github.com/techrote/RetroBar-Extreme/issues/7#issuecomment-6126564765) | PR #8, short SHA `1ae8938`. |
| UX-006 | [Native-sizing report](https://github.com/techrote/RetroBar-Extreme/issues/9#issuecomment-6127224058) | PR #10, short SHA `40455bf`; includes follow-up defects subsequently routed to UX-007. |
| UX-007 | [PASS](https://github.com/techrote/RetroBar-Extreme/issues/11#issuecomment-6128686146) | PR #12, short SHA `9e7ff3e`. |
| UX-008 | [PASS](https://github.com/techrote/RetroBar-Extreme/issues/13#issuecomment-6130777321) | PR #14, short SHA `6af9fd1`. |
| UX-003 | [Style-layer acceptance](https://github.com/techrote/RetroBar-Extreme/issues/4#issuecomment-6215917137) | Names PR #15 build, no exact full head in the report; separates owner appearance report from agent checks. |
| UX-004 | [Editor acceptance](https://github.com/techrote/RetroBar-Extreme/issues/5#issuecomment-6218017594) | Names owner-created style and later angle-control follow-up `6ffd838`; do not infer the follow-up itself was separately retested. |
| UX-009 | [Colourway acceptance](https://github.com/techrote/RetroBar-Extreme/issues/17#issuecomment-6219971124) | PR #20 scope, no exact full head in the report; clarifies automatic active-style persistence. |
| UX-010 | [Exact-head PASS](https://github.com/techrote/RetroBar-Extreme/issues/18#issuecomment-6222247337) | Full head `273f12a10fb5273c2e7e72bf7585cf8b47dd4f82`, with workflow links. |
| UX-011 | [Exact-head PASS](https://github.com/techrote/RetroBar-Extreme/issues/19#issuecomment-6223445529) | Full head `51c5695e9a5bb2b9c2907608bb4719a472ec084f`. |
| UX-012–016 | [PR #24](https://github.com/techrote/RetroBar-Extreme/pull/24) and its linked issues | Merged as `dba7b477622ebc54f47c3149a7292ed6d3f42051`; implementation/agent test records located, no separate exact-head owner PASS recovered. |
| UX-017 | [PR #30](https://github.com/techrote/RetroBar-Extreme/pull/30), [issue #29](https://github.com/techrote/RetroBar-Extreme/issues/29) | Merged as `c51ee1c97f1976cd315f7df1588d7d7911462f93`; no separate exact-head owner PASS recovered. |

Later PR/release descriptions mention daily use. That is useful context, but does not certify every UX-012–017 acceptance item or the current whole source tree. This audit does not revoke a historical acceptance, reopen completed tasks or claim new owner testing.

## Open-Shell prerequisites recovered from source

The inherited [workflow](https://github.com/techrote/Open-Shell-Menu-Extreme/blob/e1fe220d18bb38a0d8a19c70332d75fef4c2625f/.github/workflows/build.yml) only triggers PRs matching `Src/**`, `Localization/**` or the workflow path, plus manual dispatch. It has no push trigger. The manual-master path invokes SignPath and a `contents: write` release job. Missing credentials would not make those declared side effects an acceptable build-only design.

[Setup.wxs](https://github.com/techrote/Open-Shell-Menu-Extreme/blob/e1fe220d18bb38a0d8a19c70332d75fef4c2625f/Src/Setup/Setup.wxs) includes the Update feature at Level 1; [Update.cpp](https://github.com/techrote/Open-Shell-Menu-Extreme/blob/e1fe220d18bb38a0d8a19c70332d75fef4c2625f/Src/Update/Update.cpp) enables its automatic-check setting by default. [BuildBinaries.bat](https://github.com/techrote/Open-Shell-Menu-Extreme/blob/e1fe220d18bb38a0d8a19c70332d75fef4c2625f/Src/Setup/BuildBinaries.bat) copies the updater. The suite's no-updater requirement is therefore outstanding for this fork.

[StartMenu.cpp](https://github.com/techrote/Open-Shell-Menu-Extreme/blob/e1fe220d18bb38a0d8a19c70332d75fef4c2625f/Src/StartMenu/StartMenu.cpp) installs an Explorer hook and exposes an exit route; [StartMenuDLL.cpp](https://github.com/techrote/Open-Shell-Menu-Extreme/blob/e1fe220d18bb38a0d8a19c70332d75fef4c2625f/Src/StartMenu/StartMenuDLL/StartMenuDLL.cpp) contains cleanup. These source paths do not establish working install/login/uninstall/recovery on the owner's Windows version.

The repository [Actions run collection](https://api.github.com/repos/techrote/Open-Shell-Menu-Extreme/actions/runs?per_page=20) returned `total_count: 0`; [release collection](https://api.github.com/repos/techrote/Open-Shell-Menu-Extreme/releases?per_page=10) was empty. These collection URLs are live, unlike the pinned code links above. No workflow or installer was run as part of this audit. [UX-020](https://github.com/techrote/Open-Shell-Menu-Extreme/issues/1) owns the bounded adaptation and VM acceptance gate.

## Verification and remaining limits

Local validation runs `python3 scripts/check_docs.py`, the regression suite under `tests/`, and `git diff --check`. Independent review covers both factual boundaries and validator behavior. The [documentation workflow](../../.github/workflows/docs-quality.yml) runs these Python checks on the exact PR head and merged-main source with read-only contents permission, no persisted checkout credential, no package installation, a five-minute timeout and superseded-run cancellation.

The checker intentionally does not make network requests, inspect live CI, compile the module applications or test a Windows desktop. Its fixture suite exercises valid and broken paths/anchors, reference/image syntax, duplicate headings, code exclusion, URL decoding and checkout-boundary handling. Results and final commit identities belong on the integrating PR/issue, so the audit does not predict its own future CI outcome.

The separate RetroBar repair reached head `497379a10578724dcc15b8cc38c7bc2a2fca0cf6`: [build/package](https://github.com/techrote/RetroBar-Extreme/actions/runs/41754944857), [Extras](https://github.com/techrote/RetroBar-Extreme/actions/runs/41754944914), [Start colourways](https://github.com/techrote/RetroBar-Extreme/actions/runs/41754944882) and [LUT textures](https://github.com/techrote/RetroBar-Extreme/actions/runs/41754944968) all passed. Its [test card/evidence](https://github.com/techrote/RetroBar-Extreme/issues/34#issuecomment-6620164980) records 447 Extras assertions on each of .NET 6 and .NET 10; PR #35 remains draft and unmerged.

Remaining boundaries are RetroBar UX-019's owner acceptance and subsequent merge qualification, Open-Shell UX-020's build and VM qualification, and the unresolved styling/parity choices in the programme. No public release, tag, Windows deployment, new visual acceptance or whole-suite offline guarantee is created by the umbrella documentation merge.
