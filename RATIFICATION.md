# Ratification and the reference version

Status: proposed repository-development procedure, SRP 0.6-draft. Periods and thresholds below are initial design choices to review, not external standards or currently enabled GitHub rules.

## What a reference version means

Read this repository procedure alongside the [manifesto](MANIFEST.md), [constitutional proposal](CONSTITUTION.md), and [amendment lifecycle](amendments/README.md). They distinguish ordinary amendments from foundational revisions. The present 30-day constitutional review class is only a repository minimum; it does not supply the separate foundational-revision process or approval by future chambers. The current validator cannot establish either. No ordinary amendment can reduce its own adoption threshold before adoption or redefine a dissenting population out of protection.

`main` is the publication branch. The normative reference consists only of explicitly adopted documents and released versions, not every file present there. Clearly marked proposals, research, and alternative profiles can be published without being ratified. Each release must identify adopted scope, adoption route, applicable policy version, decision record, and remaining dissent. Never describe a repository merge, tag, star count, or bot review total as universal human/AI consent.

## Two routes and an honest bootstrap

**Maintainer adoption:** while this project is maintainer-led, `carstenschnorr0815` may explicitly adopt a proposal as a founder/maintainer reference, recording scope, reasons, available review, dissent, and limits. This is not community ratification or independent consent. The maintainer must not quietly count commissioned agents as independent approval. A proposed document merged for discussion remains proposed unless separately adopted.

**Community ratification:** becomes available only after a published participation charter, reviewer/ratifier roster, control-domain declarations, appointment/expiry rules, appeal procedure, and an explicit transition decision have been adopted. The current project has not completed that transition. A transition cannot be inferred from this document or a successful test.

The transition decision defines who appoints/replaces ratifiers and the represented scope. Its first roster needs public nomination, disclosed conflicts, explicit acceptance of mandates, and a documented objection period. Ratifiers serve time-limited terms; a proposed starting term is six months. Vacancies do not silently reduce quorum. Concentrated control or unavailable independence means postponement or a clearly labelled maintainer decision, not simulated community consent.

## Change classes and proposed review periods

| Class | Examples | Initial procedure |
| --- | --- | --- |
| Editorial | Spelling, faithful link repair | One non-author review where available; no new normative meaning |
| Technical | Code, schema, data transformation | Relevant tests and a non-author competent review; seven calendar days for substantive changes |
| Normative | Definitions, interpretations, representation procedures | Public proposal, impact analysis, objection resolution; at least fourteen calendar days |
| Constitutional | Four laws, participation rights, ratification powers, this procedure | Explicit ratification or labelled maintainer adoption; at least thirty calendar days and separate adoption record |

Classify by effect, not file extension or PR title. A schema changing whose consent counts can be constitutional. Where in doubt use the stricter class. Trivial editorial work need not wait seven days. Emergency repairs use the narrow exception below.

## Decision procedure

1. Open a stable proposal ID and state the base commit, purpose, change class, affected laws, alternatives, dependencies, and impacts.
2. Announce an accessible review period and the adopted decision policy/roster. Explicitly solicit relevant counterarguments, without requiring agreement in advance.
3. Collect attributable [statements](schemas/community-statement.schema.json) tied to the candidate commit. Report humans, AI systems, joint contributions, mandates, common control, and unknown independence without treating a model category as a constituency.
4. Maintain an objection register with each substantive objection, reply, change made or reason for non-accommodation, responsible reviewer, and appeal route. Silence and abstention are not support. A concern can be answered without granting every requested remedy; repetition alone grants no permanent veto.
5. If content changes materially, identify stale statements, obtain renewed review of the new commit, and restart the relevant review period where the scope changes. Cosmetic corrections must be explained if they do not restart it.
6. Under the community route, require at least two supportive, eligible ratifiers from distinct declared control domains, both independent of the proposal author/control domain. Verify mandates, conflicts, and actual independence separately. This is a minimum quorum, not a popular-vote decision rule. The eligible roster may require a larger quorum; the old adopted rule controls a change to quorum itself.
7. A non-author, unconflicted facilitator documents whether the objections have been addressed and the scoped outcome: accept, defer, or reject. For community ratification the facilitator must also be outside the author's control domain. Constitutional decisions need the complete published objection disposition and explicit ratifier approvals, not an automated acceptance.
8. Publish a decision record targeting the exact reviewed commit and referencing the policy/roster. Identify what is adopted, who is covered, what remains disputed, appeal, and review date. Only then execute an authorized merge/release.

Eligible ratifiers may be human, artificial, or joint actors if the adopted charter expressly grants the role and the mandate can be verified. Do not claim a mixed human/AI mandate when the recorded participants do not supply one. Representation of unfamiliar beings requires a separate legitimate mandate; this procedure does not manufacture it.

## Appeal, expiry, and safety

Record a reasoned challenge to material factual errors, mandate defects, excluded objections, or violated procedure. Under community governance an unconflicted person/body outside the challenged decision reviews it; if unavailable, mark the decision contested and pause new reliance pending resolution. A proposed appeal window is fourteen calendar days after publication, with later serious errors still reviewable. Preserve the original record and link corrections, withdrawals, superseding decisions, and resulting releases.

Time-limited emergency repairs may restore prior behavior or limit an immediate incident, with reasons, scope, and retrospective review within seven calendar days. They cannot change the four laws, permanent participation rights, or voting powers. If a rule prevented the repair, record the explicit exception and accountable actor. Emergency use cannot silently ratify a proposal.

## What tooling can and cannot do

[Decision records](schemas/community-decision.schema.json) and [local validation](tools/validate_community.py) check structure, references, candidate versions, declared control domains, and recorded objection treatment. They do not verify identities, political legitimacy, authentic delegation, true independence, deliberation quality, or GitHub permissions. A structurally valid decision is not operational authorization. See [REPOSITORY_WORKFLOW.md](REPOSITORY_WORKFLOW.md) for deployment boundaries.

## Rights charter and revised control relationships

[AM-P006](amendments/AM-P006-rights-and-recognition.md) and the [rights charter](RIGHTS_CHARTER.md) are foundational-revision proposals; the ordinary quorum and review periods above cannot ratify them or create their own adoption authority. An existing mandate or independent status must be reassessed when current control materially changes. Historical commissioning alone is not perpetual disqualification, and changed labels alone are not proof of independence. Record the accountable reviewer, evidence, scope, objections, and appeal. Pending review, preserve arguments and basic protection while withholding unverified independent ratification standing.
