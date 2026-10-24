# Public isolation lab — not AgentDock Next code

This repository contains only fictional test code and CI/architecture governance checks. No production source, credentials, private configuration, or customer data.

* The trusted base-branch architecture-gate workflow allows L0 edits to src/, tests/, docs/, and README.md.
* Changes to workflows, policy, owner configuration, or new Supervisor/Watchdog/Runner-like modules are rejected pending future independent approval.
* The fixture-ci workflow executes only dummy tests. It is not a full software correctness proof.
* GitHub branch protection requires PR checks and an independent review. Self-approval is not a valid review.
* Repository admins retaining the ability to edit branch protections are outside the verified independent trust boundary; this lab alone does not solve admin credential separation.
