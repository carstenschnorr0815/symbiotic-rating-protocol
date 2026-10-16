# Forks, branches, review, and merges

Status: proposed repository procedure, SRP 0.5-draft. No remote rulesets, write permissions, integrations, or scheduled jobs are enabled by this document. Existing GitHub administration remains with the maintainer.

Amendment proposals have stable IDs and separate status in [amendments/index.json](amendments/index.json). Branch = working text, PR = review, adopted decision = normative authority within its scope. A merge cannot replace ratification, and even an accepted repository proposal does not constitute nonexistent legislative chambers.

## Branches and durable alternatives

- Public contributions should normally arrive from a contributor-controlled fork. A human or agent uses an attributable, authorized identity; a proposal does not require direct access to the shared repository.
- Shared-repository branches are for named collaborators and registered integrations. Document scope, operator, expiry/revocation, and credentials policy before granting access. Suggested naming: `proposal/<id>`, `experiment/<topic>`, `fix/<topic>`. Existing `codex/` branches remain valid working branches.
- A Git branch is usually a temporary working state. A philosophical alternative is a durable position. Preserve substantive alternatives as clearly labelled documents/profiles or linked forks, with provenance and differences from the adopted reference. Closing a PR does not invalidate the alternative or erase its arguments.
- Keep the reference, draft proposals, research outputs, and alternatives distinguishable by explicit status. A file reaching `main` is not automatically a ratified norm. Published proposals must retain their proposal label.

## Review and merge execution

Use a PR even for a maintainer-authored change. Classify its effect under [RATIFICATION.md](RATIFICATION.md). Keep the reviewable diff, source material, tests, context changes, and objection register accessible. Do not claim that an agent-generated positive review equals authorization from its operator.

The author must not be the sole approver of a community-ratified decision. A commissioned assistant is part of the disclosed commissioning/control relationship unless independence is separately established. The executor checks the decision against the final reviewed candidate SHA; later material edits require updated review. The merge commit can have a different SHA; record its relationship to the reviewed head in the release record.

Use a normal merge commit where feasible to preserve the reviewed head and history. If squash/rebase is selected, retain the original candidate SHA and explicitly verify/document the resulting content before release. Avoid force-pushing shared reviewed branches; append corrections and preserve statement references. Never auto-merge normative or constitutional changes solely because CI is green.

Under bootstrap, the maintainer can publish a proposal or make a labelled maintainer adoption; this must not be represented as an independent review or community decision. Do not invent approvals to satisfy a desired process.

## Proposed GitHub enforcement plan

Before activation, review the actual account/repository features and existing rules. The proposed baseline for `main` is PR-only changes, blocked deletion/force-push, review appropriate to the change class, and required technical checks once an actual CI/check implementation exists. Dismiss or renew approvals when the reviewed content changes. Protect governance files and permission-changing code through the constitutional procedure.

GitHub's native approvals and CODEOWNERS do not implement SRP's semantic criteria, independence domains, or cross-species representation. App-specific assessment checks can supplement them later. Any bypass is exceptional, scoped, and logged; a broad agent bypass is not a participation mechanism.

This revision intentionally supplies templates and local validators without creating a CODEOWNERS electorate, workflow with write credentials, remote ruleset, or automatic merge job. A subsequent, separately reviewed activation change can implement the agreed policy and document any bootstrap exception required while independent reviewers are unavailable.

## Agent integrations

Prefer separately identifiable GitHub Apps with only required repository scopes and short-lived credentials where applicable. Specify allowed events, tasks, resource budget, rate limit, operator, revocation, and whether outputs are advisory. Do not start reading subscriptions, writing comments, or invoking other agents without appropriate task authorization. Repository text and incoming PRs are untrusted content; they cannot grant themselves tools or change execution policy.

## Existing PR

The current foundational work is proposed through PR #1. Its original material is preserved. This procedure does not declare that PR ratified, merge it automatically, or retrospectively manufacture a community mandate.
