# SRP technical specification

Version: 0.2-draft. This replaces the experimental `1.0.0-Draft` as the working proposal, not as a claim of greater validation. The [original](docs/history/initial/SPECIFICATION.md) is unchanged in history.

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
python -m unittest discover -s tests -v
```

Output is record validation and a list of findings needing review, not a rating, legal approval, or deployment instruction.
