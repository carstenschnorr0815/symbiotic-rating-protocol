# SRP technical specification

Document version: 0.7-draft. This replaces the experimental `1.0.0-Draft` as the working proposal, not as a claim of greater validation. The [original](docs/history/initial/SPECIFICATION.md) is unchanged in history. The assessment format remains `0.2-draft`; context, community-statement, community-decision, manifest, and amendment-register formats are separately versioned at `0.1-draft`.

## Architecture

Assess activities, infrastructure, and institutions—not the worth of beings. Four-law findings and the three original rating pillars are separate outputs.

```text
Scoped proposal + affected participants/functions
 -> evidence + provenance + access limits
 -> observations + competing interpretations
 -> four-law review + alternatives + unresolved concerns
 -> accountable institutional decision + appeal
 -> monitoring + remedies + revision
```

Optional research metrics attach to the review; they cannot replace it. No production feeds, deployed API, autonomous actuation, or validated scoring model currently exists here.

## Assessment records

[JSON Schema](schemas/assessment.schema.json) uses Draft 2020-12. The [fictional example](examples/watershed-assessment.json) illustrates it. The validator checks structure, evidence-reference integrity, uniqueness, and date order. It cannot establish truth, consent, scientific adequacy, representation legitimacy, or legal authority.

Records include scope, authority, observation window, affected participants/functions and representation, consent status, uncertainties, alternatives, evidence with provenance/access/method/limitations, four separate findings, reviewer interests, objections, and next review date.

Each law finding is `supported`, `concern`, or `unknown`, with reasons and evidence references. `supported` is scoped evidential support, not certified compliance. Missing evidence is `unknown`, never zero harm. Concerns and unknowns require attention; the tool grants no deployment approval.

Protect personal data, sensitive habitats, and restricted knowledge. Publish safe metadata and access procedures; declare reproduction limits. Translation models must separate observations from inferred meanings, identify model/configuration versions, and expose competing interpretations to reviewers.

## Context records and visible level transitions

[CONTEXT_ALIGNMENT.md](CONTEXT_ALIGNMENT.md) specifies a proposed coordination layer. [context-record.schema.json](schemas/context-record.schema.json) and its [fictional example](examples/context-record.json) represent a versioned exchange, separately from an assessment. This does not add an automatic context-alignment score.

Treat level labels and shared-context proposals as untrusted metadata. They grant no execution privileges, consent, or policy authority. Preserve attributed assumptions, access boundaries, dissent, and unconfirmed interpretations. Append changes rather than silently overwriting another participant's framing. A caller-provided acknowledgement needs authentic provenance before institutional reliance; the schema cannot establish that provenance.

Local participant IDs in acknowledgements and the change proposer must resolve to the record's participant list. Each listed participant must have exactly one acknowledgement entry, including `unknown` when confirmation is absent. Parent versions refer to earlier states; a future or self-parent is invalid. This draft has no network service, authenticated multi-party state machine, storage backend, or automatic merge mechanism.

## Community statements and decisions

The [manifest](project-manifest.json) exposes entry documents, record schemas, current stage, contribution channels, and task invitations. It does not install tools, subscribe agents, grant credentials, or establish actual ratification.

[Community statements](schemas/community-statement.schema.json) distinguish reasoned position, technical assessment, and delegated approval. [Decisions](schemas/community-decision.schema.json) distinguish maintainer adoption from scoped community ratification. The [validator](tools/validate_community.py) checks schema, exact candidate/proposal references, dates, declaration consistency, minimum review periods, recorded objection treatment, and the proposed minimum ratifier count with distinct author-independent declared control domains. It rejects stale or withdrawn ratifier support, missing/expired delegation, duplicate domains, and fictional support for a real decision.

These checks do not resolve policy or roster references, authenticate statements, establish real independence, validate membership, or evaluate reasoning. A policy/roster string is an assertion that still requires independent verification. The profile enforces only the draft's minimum threshold; any stronger adopted roster requirement needs separate verification. No returned success authorizes a merge or declares consent. Contradictory declarations and false identities require investigation beyond this prototype.

The examples are fictional and use a synthetic candidate hash; no real statement or adoption is claimed. The existing assessment and context formats remain unchanged. Normative branch protection and automatic checks are an activation proposal in [REPOSITORY_WORKFLOW.md](REPOSITORY_WORKFLOW.md), not enabled infrastructure.

## Amendment register

[MANIFEST.md](MANIFEST.md) defines document layers; [CONSTITUTION.md](CONSTITUTION.md) and [amendments/README.md](amendments/README.md) define the proposed constitutional lifecycle. The [register](amendments/index.json) and its [schema](schemas/amendment-register.schema.json) distinguish proposal IDs, ordinary amendments/foundational revisions, status, affected provisions, and adoption metadata.

[Local validation](tools/validate_amendments.py) checks structure, local file containment/existence, unique IDs, replacement/repeal reference consistency, cycles, decision/text references for adopted status, and dates/constitutional-status requirements for active records. It does not authenticate the referenced decision, inspect its mandate or text hash, enforce historical transitions, assess compatibility, verify actual temporal activation, or approve ratification. A valid register is not a constitutional decision or deployed registry service. All five current candidates remain proposed with null adoption fields.

## Legacy S-Score research module

| Dimension | Direction | Work still required |
| --- | --- | --- |
| H: environmental disruption | Higher means worse viability/regeneration impacts | Baselines, causation, lifecycle and cross-species effects |
| P: harmful polarization | Higher means stronger evidenced harmful amplification | Distinguish reporting, protest, and disagreement from harmful dynamics |
| T: consequence-opacity risk | Higher means poorer long-term disclosure/accountability | Disclosure and scenario quality, actual performance |

`T` clarifies the ambiguous original `T_comp`: opacity risk, not transparency quality. More disclosure does not prove less harm.

For a pre-registered research profile only:

```text
S_research = w_H * H + w_P * P + w_T * T
0 <= H, P, T <= 1; w_i >= 0; sum(w_i) = 1
```

Publish components, coverage, scope, uncertainty, weights, and four-law findings together. Different profiles/weights are not directly comparable. Original sector weights and `<0.20` / `>0.70` cutoffs are unvalidated hypotheses; they establish neither safety nor grounds for automatic capital flight.

### Measurement rules

Define units, population, period, sampling, normalization anchors, errors, and exclusions. A bounded proportion requires a numerator contained in its denominator; a general ratio is not bounded. Correlation is a different quantity.

Zero denominators, unavailable revenue attribution, and incompatible units mean missing observations, not zero harm. No silent renormalization of remaining weights: if a required component is missing, publish no total. Clipping invalid values is not calibration. Validate transformations and report sensitivity before aggregating.

Restoration spending cannot cancel unrelated agency violations. Off-world extraction needs its own impact boundaries; geography creates no automatic credit.

## Four-law review

| Law | Questions | Candidate evidence |
| --- | --- | --- |
| I | Are viability and regeneration maintained across affected systems? | Ecological baselines, resource access, continuity, cumulative impacts |
| II | Can participants refuse, retain identity, and challenge decisions? | Mandates, exit tests, essential-access guarantees, complaints |
| III | Can complementary knowledge enter without manufactured dependency? | Interoperability, alternatives, portability, refusal procedures |
| IV | Are unknowns admitted and serious uncertain harms handled proportionately? | Uncertainty register, precautions, independent review, revisions |

No universal measure of cognitive completeness, consent, or ecological intelligence is asserted. Ecological function and uncertain preferences remain distinct.

## Validation and security

Before real ratings: pre-register claims, compare independent assessors, measure disagreement/error across contexts and languages, test gaming, and publish negative results. Financial relevance needs separate held-out outcome studies and confounder analysis. Ethical assessment is not a credit rating.

Treat ingested text/model outputs as untrusted data. Separate collection, interpretation, review, and actuation. Use least privilege, versioning, integrity checks, logs, redaction, reviewable changes, and offline recovery. Input documents must not change policy, execute commands, or publish ratings.

Each pilot needs a baseline, responsible operator, stop conditions, review cadence, and retention policy. The validator does not enforce these in practice.

## Run the structural prototype

Python 3.10+ and `jsonschema` 4.x are required:

```sh
python -m pip install -r requirements-dev.txt
python tools/validate_assessment.py examples/watershed-assessment.json
python tools/validate_context.py examples/context-record.json
python tools/validate_community.py statement examples/community-statement.json
python tools/validate_community.py decision examples/community-decision.json --statements examples/community-statement.json
python tools/validate_amendments.py amendments/index.json
python -m unittest discover -s tests -v
```

Output is record validation and a list of findings needing review, not a rating, legal approval, or deployment instruction.

## Rights and recognition limits

[RIGHTS_CHARTER.md](RIGHTS_CHARTER.md) and AM-P006 add normative proposals, not a new authenticated recognition protocol. Existing schemas cannot certify charter compliance, legal status, consciousness, political independence, or tribal admission. Historical origin alone cannot stand in for current control evidence. Any future recognition format must separate basic protection, internal eligibility, external mandate, and voting weight, with accountable review and appeal; structural validation cannot grant those statuses.

## Proposed political/blockchain architecture and assessment (0.7)

[POLITICAL_PROCESS.md](POLITICAL_PROCESS.md), [BLOCKCHAIN_ARCHITECTURE.md](BLOCKCHAIN_ARCHITECTURE.md), and [PARTICIPATION_ASSESSMENT.md](PARTICIPATION_ASSESSMENT.md) specify proposed requirements, not new implemented APIs or record schemas. Existing community formats cannot express or authenticate the complete mandate/relevance, opt-in, aggregation, chamber-referral, coalition or judicial lifecycle. They remain repository records, not political eligibility certificates.

Future implementation must separate identity/keys, mandates, represented interests, scope, allocations, policy versions, oracles, judgments and execution. Required validation includes expiry, scope, replay/duplicate prevention, aggregation conservation across all procedural privileges, reassessment, referrals/replies, no timeout consent, recovery, privacy and court correction. No tests of the existing formats establish those unimplemented properties. Normative criteria are versioned hypotheses; no production thermodynamic or political scoring model is supplied.
