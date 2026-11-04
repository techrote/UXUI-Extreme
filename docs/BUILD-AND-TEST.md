# Builds and owner testing

**Snapshot checked 4 November 2026.** These instructions distinguish the two modules and the evidence they actually have. The owner receives a usable download and a short test card; agents perform builds and investigate failures.

## RetroBar — choosing a build

Inspected source: [`65b36c0fba6ef8d8e44294b3ea332b03e32f638c`](https://github.com/techrote/RetroBar-Extreme/commit/65b36c0fba6ef8d8e44294b3ea332b03e32f638c). The [RetroBar workflow run](https://github.com/techrote/RetroBar-Extreme/actions/runs/39116769177) completed successfully for that exact push. For a different task or newer PR, use that task's own source and artifact, not these historical links.

| Download | Contents / use |
|---|---|
| [RetroBar Portable 64-bit — CI artifact](https://github.com/techrote/RetroBar-Extreme/actions/runs/39116769177/artifacts/12132522901) | Windows x64, .NET 10 framework-dependent portable build. This is the direct baseline CI artifact for the owner's x64 Windows 11 machines. |
| [RetroBar Portable — aggregate CI artifact](https://github.com/techrote/RetroBar-Extreme/actions/runs/39116769177/artifacts/12132687761) | Architecture subfolders, including separate Win7-8 builds. Select the matching architecture/framework; do not use the legacy folder just because it is present. |
| [v1.23.43-extreme-delta.1 prerelease](https://github.com/techrote/RetroBar-Extreme/releases/tag/v1.23.43-extreme-delta.1) · [portable asset](https://github.com/techrote/RetroBar-Extreme/releases/download/v1.23.43-extreme-delta.1/RetroBar-Extreme-Portable.zip) | Published personal test package. The tag resolves to the inspected source. This audit checked metadata, not a byte-for-byte equivalence or new Windows execution of the release ZIP. |

GitHub CI artifacts may require sign-in. The two listed artifact records were unexpired and scheduled to expire on **16 January 2027** when inspected. If an artifact expires, an agent must supply a new source-bound build; a similarly named archive does not establish equivalence.

## RetroBar — prerequisites and settings

The normal Windows 11 CI portable build requires the matching **.NET 10 Desktop Runtime**, including the correct architecture. Microsoft's [.NET 10 download page](https://dotnet.microsoft.com/en-us/download/dotnet/10.0) has the Windows Desktop Runtime installers. The generic .NET/ASP.NET runtime is not the WPF desktop runtime. The project's portable publish profile has `SelfContained=false`; the workflow selects `net10.0-windows` for normal Windows 11 artifacts. [Profile](https://github.com/techrote/RetroBar-Extreme/blob/65b36c0fba6ef8d8e44294b3ea332b03e32f638c/RetroBar/Properties/PublishProfiles/x64-portable.pubxml), [workflow](https://github.com/techrote/RetroBar-Extreme/blob/65b36c0fba6ef8d8e44294b3ea332b03e32f638c/.github/workflows/retrobar.yml).

**Portable does not isolate settings.** Builds read/write `%LOCALAPPDATA%\RetroBar\`, including `settings.json`, `Style.json`, `Styles\` and user assets. Before replacing a daily executable or testing persistence, close RetroBar and preserve that folder and the previous executable. Do not run competing copies as a substitute for isolation. A named style export alone does not include font/layout/theme settings. [Path helper](https://github.com/techrote/RetroBar-Extreme/blob/65b36c0fba6ef8d8e44294b3ea332b03e32f638c/RetroBar/Extensions/ManagementExtensions.cs).

The inspected baseline still checks upstream RetroBar for updates. **Check for updates = off** mitigates the application's polling on that older build. Its installer has a separate upstream probe; the portable route avoids that installer code. [UX-019](https://github.com/techrote/RetroBar-Extreme/issues/34) tracks the source repair, including legacy saved settings. Do not describe the baseline as already offline-policy compliant.

Quitting RetroBar normally restores Windows' taskbar. Include that as an observed acceptance step for each relevant build; this source audit does not establish crash, forced-termination or Windows-update recovery. Keep a working way to start Task Manager and the previous build available during a shell test.

## A short owner test card

For each task, the agent supplies one card with these fields, already filled with real values:

| Field | Required content |
|---|---|
| Download | Direct CI artifact link, source SHA, architecture and runtime prerequisite. |
| Try | A few concrete actions relevant to the issue, including restart/restore if persistence or shell ownership changes. |
| Good | Observable expected behavior; state the relevant Windows build, DPI/taskbar scale and theme. |
| Reply | PASS/FAIL with the tested SHA; request a screenshot only when it helps judge appearance. |

The card is a handoff format, not a new request to test the historical baseline. No stack-trace investigation or local compilation is assigned to the owner. Record the actual reply on the owning issue; do not turn a compiled or automated-tested result into owner-tested.

## Open-Shell — qualification before a daily-machine build

At inspected [`e1fe220`](https://github.com/techrote/Open-Shell-Menu-Extreme/commit/e1fe220d18bb38a0d8a19c70332d75fef4c2625f), the inherited [workflow](https://github.com/techrote/Open-Shell-Menu-Extreme/blob/e1fe220d18bb38a0d8a19c70332d75fef4c2625f/.github/workflows/build.yml) runs for path-filtered PRs to `master` or manual dispatch, not for every documentation PR or every push. It declares `OpenShellSetup*.exe`, `OpenShellSymbols*.7z` and `Utility.exe` outputs. **There is no declared portable application ZIP.** The symbols archive is not a runnable package.

No fork workflow run or release was available in the audit. Manual dispatch on `master` includes SignPath signing and a prerelease/tag job; do not run that path unchanged as a build-only check. The inherited installer also includes an updater enabled by default. Those are concrete source discrepancies with suite policy, tracked in [UX-020](https://github.com/techrote/Open-Shell-Menu-Extreme/issues/1).

Before an owner test, that module task must provide:

- An unsigned, non-publishing CI path with successful source-bound build/contract evidence and a post-merge qualification route.
- A usable installer whose updater inclusion/startup behavior meets suite policy. Do not claim portable support without implementing and qualifying it.
- A Windows 11 snapshot-VM record covering installation, startup/login, menu use, exit, uninstall and stock-shell restoration, with the exact OS build and module version.
- For RetroBar pairing, both source SHAs and settings for menu opening, placement and Windows-key behavior. Source recognition in RetroBar is not an end-to-end test.

Open-Shell's Explorer hooks and cleanup functions were reviewed, not executed here. The same VM-first requirement applies to any later Explorer-injecting skinning module.

## Agent validation boundaries

The umbrella's [documentation workflow](../.github/workflows/docs.yml) validates local Markdown links/anchors and exercises the validator with intentionally broken fixtures. It is read-only, offline after checkout, has a bounded timeout and cancels superseded runs. It does **not** compile either Windows module or poll their live status.

The validator supports ordinary inline/reference links and images, GitHub-style Markdown heading fragments and duplicate headings. It skips code fences/spans and external URLs. It is not a complete CommonMark/HTML/MDX renderer; container-specific/indented code and raw HTML navigation need review if introduced. Its [fixture tests](../tests/test_check_docs.py) define the supported cases.

When refreshing evidence, fetch the module's actual default branch, PR/issue state, run source/conclusion and artifact metadata. Keep the old dated audit as history and update the overview with the new checked date. Do not invent an acceptance result to make the tables agree.
