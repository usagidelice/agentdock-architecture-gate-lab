# GitHub Identity Cutover — Consolidated Design Review

Status: PROPOSAL ONLY — no production change authorized.  
Scope: public synthetic `agentdock-architecture-gate-lab` and future AgentDock Next GitHub development boundary only.  
G0/G1: HOLD until the evidence gates below pass. No change to Core 1.1.0, Next three-node runtime, Legacy, or existing owner identities.

## 1. Verified current boundaries

| Principal / surface | Observed capability | Assessment |
|---|---|---|
| GitHub App `usagidelice-next-lab-dev-2026` | Installed for **selected lab repository only**; bot PR #6 created and merged after independent human approval | Restricted identity flow proven in LAB |
| GitHub Actions `lab-trusted-app` | Environment restricted to protected branches; environment secret used by successful workflow run 40118305269 | App token mint and admin-denial proof PASS in LAB |
| Protected lab `main` | Required `architecture-gate` and `fixture-ci`, independent review, admins enforced, force push/deletion prohibited | Real post-bootstrap direct write denied 409 |
| ChatGPT GitHub connection | **All repositories** installation selection; `Allow low-risk actions` interaction mode; admin rights observed on lab repo | HIGH: UI approval mode is not a repository or API scope boundary |
| M1 Next command runner | Runs as workstation OS user; `gh` uses owner's `usagidelice` login with `repo` OAuth scope | HIGH: executable owner capability reachable from agent |
| Intel Next command runner | `gh` installed, no active login observed | Lower exposure; not a proof of full isolation |
| Dell Next container | No `gh` executable and no common GH_* credential env vars observed | Lower exposure; container runtime boundary still needs focused review |
| PEM / browser sessions | Complete cross-directory file and browser-profile inventory not established | UNKNOWN: cannot claim credentials are absent |

**Do not conflate** a successful GitHub App bot smoke test with isolation of all GPT-accessible owner credentials.

## 2. Intended risk classes and authorities

| Class | Examples | Execution policy | Hard boundary |
|---|---|---|---|
| L0 | Read permitted source, PR metadata, test status, logs without secrets | Automatic | Repository allowlist, least-privilege read token |
| L1 | Edit synthetic or approved development branch; unit tests; propose PR | Automatic within approved task scope | Bot installation token; no workflow, admin or secret access; PR required |
| L2 | Merge into protected `main`, modify shared trusted CI, production release | Human gate | Server-side required checks + independent human review; specific authorization for workflow bootstrap/deploy |
| L3 | Delete repository, change permissions, rotate/revoke keys, disable protections, destructive rollback | Separate explicit authorization | Human-only administrator identity, outside agent accessible runtime |

`Allow low-risk actions` is a ChatGPT interaction preference, **not** a guaranteed four-class enforcement engine. Enforce the matrix in GitHub and OS boundaries, not only in instructions.

## 3. Target identity / trust graph

1. **Human owner**: holds GitHub account administrative authority and approval capability only in a device/user/browser profile not accessible through AgentDock. No owner PAT, OAuth token, keychain session, browser login, or PEM in the agents' runtime.
2. **ChatGPT GitHub connector**: limit installation to explicitly designated development repositories. If it cannot be restricted sufficiently, disconnect this owner-scoped connector when a tested restricted replacement is available. Read/approval preferences alone are not a privilege cap.
3. **M1 primary / Intel secondary**: can run approved local tests and create candidate artifacts without access to the owner's GitHub auth. M1's existing `gh` owner session must be deauthorized in a separately approved cutover. Reconfirm actual OS-user isolation; `gh auth logout` alone does **not** prevent use of other same-user browser/keychain credentials.
4. **GitHub App bot**: installed on *selected* repositories, `Contents: write` and `Pull requests: write` only when required to open a development PR. Mint repo-scoped, short-lived tokens in a trusted GitHub Actions job, never persist them in Next or logs.
5. **Trusted workflows**: defined on protected `main`, use `lab-trusted-app` or future equivalent environment secret, explicit repository/job permissions, no PR-supplied code or shell with secrets. Normal PR workflow-file changes are rejected by `architecture-gate`. Any intentional trusted workflow change uses a separately approved one-time bootstrap with immediate protection restoration.
6. **GitHub platform**: required CI checks source-pinned to GitHub Actions, strict current-head verification, independent human review before merge, force-push and deletion denied.

## 4. One concentrated cutover, not per-rule patches

**Stage A — preparation / read-only:** enumerate *which* repos owner ChatGPT connector must retain, inventory actual usages of M1 `gh` outside Next without reading credentials, identify user-controlled human-only review device, and inspect accessible GitHub browser/keychain exposure by metadata only. Mark unresolved findings UNKNOWN.

**Stage B — connector restriction, separately approved:** switch ChatGPT GitHub App from `All repositories` to `Only select repositories` with explicit allowlist. Test normal L0 reads and verify unselected repos are genuinely denied. If not supported, stop; do not claim technical isolation. Rollback only via deliberate repository selection adjustment.

**Stage C — workstation credential separation, separately approved:** protect human owner session outside Next-enabled OS users/profiles; authorize and deauthenticate M1's owner `gh` login. Confirm `gh api user` cannot authenticate from M1 AgentDock, even when the direct command tool is used. Review remaining same-user keychain/browser OAuth reachability. If still reachable, dedicated OS execution-user separation is required for high assurance and must be independently planned and approved; **do not** reconfigure Next services without consent.

**Stage D — restricted development workflow:** use bot for L1 GitHub branch/PR operations in an explicitly selected lab-only fixture. Keep raw private key only in the protected Actions environment, app tokens ephemeral, and workflow changes under special human-controlled bootstrap. Do not extend installation scope to Next or any business repo without approval.

**Stage E — end-to-end rejection/acceptance tests:** verify unauthorized admin access and protected-main direct writes fail; bot PR works; CI and human approval are indispensable; approved PR merges; rollback evidence and Next/Legacy isolation remain intact.

## 5. Required acceptance evidence

- G-ID-01: no `All repositories` connector installation available to agent; test inaccessible repo denial (without modifying that repo).
- G-ID-02: M1 Next command tool cannot authenticate as owner; cannot reach an equivalent owner login through accessible host credentials/browser profiles.
- G-ID-03: Intel and Dell remain free of owner capabilities under their execution identities; record actual isolation, not absence of `gh` alone.
- G-ID-04: bot token has only repo-scoped development rights; admin, secrets, workflow modifications denied.
- G-ID-05: real lab PR authored as App bot, both required checks PASS, before approval merge BLOCKED, after owner review merge permitted.
- G-ID-06: after any exceptional admin bootstrap, all branch protection flags restored and direct-write rejection reverified.
- G-ID-07: Next Core 1.1.0, its three existing connectors, existing plugins and Legacy remain unchanged and relevant pre/post health checks PASS.
- G-ID-08: old/stale PEM and tokens revoked **only after** user-approved key rotation and replacement authentication proven.

## 6. Explicit stop / rollback rules

- STOP if scope of GitHub connector permissions is not controllable or if human owner access would become unavailable.
- STOP if `gh` is found necessary for an unrelated active project; obtain a user-approved workaround first.
- STOP if the bot requires administration/workflow permissions, secrets in PR contexts, or a second orchestration service.
- Keep human GitHub recovery/login device outside all AgentDock runtimes; recovery is manual sign-in, not re-injecting a persistent owner token into AgentDock.
- Every action that revokes tokens, reduces repository installations, changes OS accounts, modifies branch rules, deploys or merges remains independently approval-gated.
- No changes to production Next/Legacy, OAuth, Docker or Core; G0/G1 HOLD until acceptance evidence is complete.

## 7. Current decision request

Approve a *separate* scope-reduction stage only after confirming the exact repositories ChatGPT GitHub must continue to access. Do not disable current connections or logout M1 as a side effect of approving this design document.
