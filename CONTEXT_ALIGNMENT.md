# Context Alignment and cognitive symbiosis

Status: coordination proposal, introduced in SRP 0.3-draft, 16 October 2026. Based on the author's [German discussion draft](docs/sources/2026-10-16-context-markers-original.de.txt), preserved unchanged. Technical formats and safeguards below are editorial proposals, not a deployed protocol or evidence that alignment has been achieved.

## The problem: correct answers at incompatible levels

Participants can answer the same words differently because they interpret different levels, boundaries, goals, or background assumptions. More information does not automatically resolve this. A proposed coordination task is to expose enough of the models behind an exchange to locate the mismatch.

The source example asks how to support multiple information objects per API. The question might concern a data structure, component responsibility, dataflow placement, conceptual modelling, maintenance roles, or a strategic information architecture. These are different questions connected by the same words. A strategic regulatory reference in the source is an example of scope, not a verified compliance claim.

| Suggested marker | Level in the source example | Question being addressed |
| --- | --- | --- |
| `[CODE]` | Methods and data structures | What implementation changes? |
| `[COMPONENT]` | Module responsibility | Which component owns the change? |
| `[PIPELINE]` | Data flow | Where is the object introduced or transformed? |
| `[ARCHITECTURE]` | Domain and system model | What does an API represent and relate to? |
| `[ORGANIZATION]` | Roles and maintenance | Who can maintain which information? |
| `[STRATEGY]` | Goals and external constraints | Which wider purpose does the architecture serve? |

These markers are a starting vocabulary for human/technical work, not a universal ontology or a hierarchy of cognitive worth. A message can involve several levels. A participant can mark a level as unknown, reject a proposed framing, or propose a domain-specific level with a definition and version. Silence does not confirm a label.

## Dynamic and asymmetric context

Treat a context as a revisable working state:

```text
Context A + a question/observation
 -> interpretation + reply + newly exposed assumptions
 -> proposed Context B
 -> participant responses, corrections, or unresolved differences
 -> next bounded working context
```

Not every reply changes the agreed state. A proposed change remains proposed until its relevant acknowledgement is recorded. A model may infer a level, but it must label that inference rather than attribute it as another participant's intention.

Accessible context differs by participant and situation. Neither humans nor AI necessarily have the repository, history, institutional knowledge, prior conversations, or observations available to the other. Record access boundaries rather than assuming that a named tool or model can see everything. Distinguish unavailable, undisclosed, unknown, and disputed information.

## Principles, with agency safeguards

1. **Make relevant levels explicit.** Use markers when they resolve a consequential ambiguity. Multi-level statements and unclassified observations are valid.
2. **Expose the basis of a contribution.** State relevant assumptions, evidence, uncertainty, and scope. This is not a requirement to disclose private cognition, internal model processes, confidential data, or protected knowledge.
3. **Make context changes visible.** Record what changed, why, which version it changes, and whose acknowledgement is pending. A switch to strategy must not silently replace a request about code.
4. **Coordinate through compatible representations.** Preserve individual and alternative models. Shared models serve the stated task; they have no automatic priority over a participant's values or identity.

These are proposed readings of the source's four principles, not changes to the four laws. Their relationship is:

| Law | Coordination contribution | Constraint |
| --- | --- | --- |
| I | Make resource and viability assumptions visible | Agreement on a model is not evidence of ecological safety |
| II | Allow correction, refusal, selective disclosure, and withdrawal | Shared context cannot override self-determination |
| III | Enable complementary models to interact | Compatibility does not require assimilation or engineered dependence |
| IV | Record inaccessible meanings, translation limits, and uncertainty | A fluent translation is not proof of mutual understanding |

## Minimal exchange procedure

1. Identify purpose, participants, decision scope, accessible context, and material gaps.
2. Propose the relevant level(s) and an explicit interpretation of the request.
3. State assumptions and the evidence or observations on which the reply rests.
4. When changing level or assumptions, propose a new context version and explain the difference.
5. Record each participant's acknowledgement as confirmed, disputed, or unknown. Confirmation covers only the specified scope; it is not agreement with the conclusion or consent to action.
6. Preserve unresolved alternatives and the ability to return to earlier contexts. Consequential decisions use the separate governance procedure and authority checks.

For low-impact reversible work, a labelled assumption can support continued work without waiting for agreement on every sentence. Missing authority, required consent, or a serious unresolved safety concern cannot be bypassed by a context marker.

## Functional joint systems and broader civilization

The source proposes the human–AI system as a possible functional organization level coordinated through models, state spaces, and protocols. This is a conceptual hypothesis. It does not prove that biological endosymbiosis entails political integration or that a new collective subject exists.

The same coordination question can be asked across species, intelligences, and organism-established functions. Start from observations and situated knowledge; maintain competing translations; indicate whether a represented participant can actually confirm an interpretation. Where reciprocal confirmation is unavailable, preserve uncertainty and accountable representation. Ecological participation through a function need not be deliberate collaboration.

Different timescales, sensory modalities, spatial boundaries, and individual/collective identities may resist the six technical markers. Adapt the vocabulary to the domain and document limits. Do not require a whale, tree, or ecosystem to use human categories to receive consideration.

## Practical entry points

For community development, [participation](PARTICIPATION.md) and [ratification](RATIFICATION.md) preserve the distinction between framing confirmation, substantive position, scoped delegation, and institutional decision. Shared control and task commissioning remain part of the declared context; they cannot disappear when a model produces a fluent endorsement.

- Architecture reviews: mark whether a change concerns code, domain semantics, organization, or strategy; retain links between the levels.
- Institutional deliberation: distinguish observations, proposed value choices, delegated authority, and implementation decisions.
- Research and translation: keep observation, interpretation, confirmation, and consent as separate records.
- Operational handovers: publish versioned context summaries with access limits, unresolved differences, and a responsible custodian.

Existing meeting records, change requests, architecture decisions, version control, and review workflows are possible implementation vehicles. These are design adaptations; the source does not establish their effectiveness.

## Technical profile and evaluation

The proposed [context-record schema](schemas/context-record.schema.json) describes a single versioned exchange; the [fictional record](examples/context-record.json) illustrates a strategy-to-architecture correction. Its schema version is `0.1-draft`, independent of the unchanged assessment format `0.2-draft`.

The record contains a context ID and version, optional parent version, level vocabulary, scope, declared access, proposed changes, participants' acknowledgement status, assumptions, evidence references, and unresolved issues. It is an exchange record, not a schema of a participant's mind. A populated record does not prove truth, completeness, mutual understanding, consent, or authority. Storage integrity, authentic attribution, parent-version resolution, and institutional checks require additional implementation.

Run `python tools/validate_context.py examples/context-record.json` after installing the existing development requirements. This checks schema conformance and local reference/version consistency. Evidence strings and parent records are not externally resolved; authenticity and the truth of an acknowledgement remain outside its scope.

Test the hypothesis before claiming that markers reduce misunderstanding. Compare similar tasks with and without markers; measure independent reviewer agreement about intended levels, correction effort, unresolved misunderstandings, time overhead, and access burden. Include deliberate multi-level questions, strategic disagreement despite matched levels, misleading labels, untranslatable observations, and false confirmation. Do not optimize for superficial agreement or replace the S-Score with an alignment score.

## Open questions

- Who defines a level vocabulary and can contest it?
- When does a shared representation help, and when does it erase a useful difference?
- What counts as reciprocal confirmation across different embodiments and timescales?
- How can context be portable without exporting protected knowledge?
- How should responsibility be allocated in a functional joint system while preserving each participant's agency?

The proposal supports bounded coordination, not a claim that all intellects can eventually share one complete model of reality.
