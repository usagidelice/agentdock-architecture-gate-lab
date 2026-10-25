# GitHub App developer identity — isolated lab setup (DRAFT)

This file contains **no credentials** and applies ONLY to the public synthetic fixture repository `usagidelice/agentdock-architecture-gate-lab`.
It is not permission to change AgentDock Next, Legacy, real commercial code, or production services.

## Goal

A *dedicated installation identity* creates branches, commits and PRs. The human account `usagidelice` alone reviews and merges.
The existing trusted GitHub Actions checks `architecture-gate` and `fixture-ci` remain required, alongside an independent human approval.

## Manual GitHub App registration

Visit https://github.com/settings/apps/new while logged in as `usagidelice`.

- Suggested unique App name: `usagidelice-next-lab-dev-2026` (adjust if taken).
- Description: `Restricted development bot for isolated public architecture gate tests only`.
- Homepage URL: https://github.com/usagidelice/agentdock-architecture-gate-lab
- Webhook: **Active unchecked**; no webhook URL or server needed for this proof.
- User authorization / OAuth login: **not needed**.
- Repository permissions: **Contents = Read & write**; **Pull requests = Read & write**; **Metadata = Read-only** (mandatory default). Leave **Administration, Workflows, Actions, Secrets, Environments, Deployments, Checks, Issues = No access**.
- Organization permissions and account permissions: **No access**.
- Installable only **on this account**.
- After app registration, use **Install App**, select `usagidelice`, **Only select repositories**, then select only `agentdock-architecture-gate-lab`. Do not install on any other repositories.
- **Do not generate or upload a private key at this stage**; first verify the app registration and selected-repository installation.

## Verification after registration (no secrets)

Report only the public App name or public App ID here. Independently verify installation includes exactly the lab repo, permissions have no Administration, Workflows, Secrets or Actions write access, and there is no user OAuth authority.

A separate user-approved design is required before minting any short-lived installation access token or deploying a signing mechanism. A GitHub App's PEM private key must never be sent through chat, placed in a repository, added to an AgentDock workspace, or exposed to `exec_command`.

## Planned live evidence sequence

1. App installation identity creates a new L0 PR in the lab from a disposable branch. **The PR author must be the `[bot]` identity**, not `usagidelice`.
2. Confirm `architecture-gate` and `fixture-ci` checks ran as GitHub Actions and succeeded on the exact head commit.
3. Attempt to approve the bot PR as `usagidelice`, confirming GitHub accepts an independent human review for a real bot-authored PR.
4. Verify a forbidden Supervisor module and a change to `.github/workflows/**` are refused by the trusted base-branch gate; inspect check creator App ID.
5. Attempt branch-protection/admin-config changes **using the limited App identity**, expect GitHub to refuse. Do NOT make this attempt with the human admin credential to claim isolation.
6. Compare source commit SHA, CI run ID, protected base and review receipt before any merge. Actual merge requires separate explicit permission.

## Critical unsolved privilege boundary

The current ChatGPT GitHub connector and Mac M1's host `gh` CLI can use the owner's administrator identity. The Core `exec_command` tool is not sandboxed. Therefore **simply installing a limited GitHub App is not sufficient to prevent a GPT tool from using the older administrator credential**. Before calling this enforced protection in production:
- Keep human admin auth outside any GPT/AgentDock-accessible process, including CLI keychain credentials and connected admin-authorized GitHub tools.
- Use separate OS/service identities and verifiable restrictions for the developer token; no new Runner or Supervisor is needed.
- Re-test real attempted bypass from **all available GPT tool paths**.
- If these boundaries cannot be proven, label result `REVIEW_WORKFLOW_ONLY`, not `SECURITY_ENFORCED`.

## Existing evidence / status

- Public lab has required Actions check contexts bound to GitHub Actions App ID, one human review required and branch protection enforced for admins.
- Existing PR #1 is authored by the owner's own identity and cannot self-approve; #2 and #3 have expected failing architecture checks.
- **GitHub App is NOT YET registered or installed.**
- AgentDock Next G0/G1 remain HOLD. No production change authorized.

Documentation:
- https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/registering-a-github-app
- https://docs.github.com/en/apps/using-github-apps/installing-your-own-github-app
- https://docs.github.com/en/apps/creating-github-apps/about-creating-github-apps/best-practices-for-creating-a-github-app
