# Proposed blockchain implementation architecture

Version: 0.7-draft. Design proposal only: no chosen chain, deployed contracts, funded wallets, identity service, issued credentials, subscriptions, or executable political authority. The user proposes blockchain-based implementation. The [constitutional process](POLITICAL_PROCESS.md) defines legitimacy independently of a particular ledger; code cannot amend rights by execution.

## Records and separated powers

Separate identity attestations, version-specific opt-in, tribal membership, scoped/self-representative or trustee mandates, coalition commitments, representation allocations/aggregation, candidate decisions, chamber referrals/replies/confirmations, court orders, and versioned assessment policies. The [adaptive research method](PARTICIPATION_ASSESSMENT.md) does not supply authenticated physical data or an allocation algorithm.

Each authority-bearing record needs identifiable issuer and subject, authority/policy reference, scope, version, validity/revocation, provenance, and independent challenge route. A useful mandate dimension is representative × represented interests × decision scope × power × validity interval. Preserve the distinction between actual consent, trusteeship, identity authentication, and decision competence. An external institution's identity attestation supplies none of the other powers automatically.

Enforce declared expiry, scope, duplicate-use constraints, eligibility snapshots, policy version, authorization signatures, and traceable transitions where technically implemented and tested. Coalition membership does not enlarge a scoped mandate. Wallet/token counts do not determine tribal voting weight. Splits/mergers conserve the relevant allocation and procedural privileges until a duly adopted reassessment changes them.

## Evidence, privacy, and external judgments

Keep sensitive identity, habitat, behavioral, and private deliberation data off a public ledger. Publish only necessary attestations/references and appropriately protected evidence commitments; a hash can still reveal linkability or permit guessing and is not automatically anonymous. Specify access, retention/deletion duties, availability, and correction. Do not require a public legal-name registry for political participation.

External facts and interpretive judgments require accountable inputs/oracles. Cryptographic provenance verifies a statement's source and integrity, not the truth of pig preferences, voluntary consent, current independence, ecological causation, or constitutional legitimacy. Separate evidence collection, interpretation, authorization, and execution; multiple inputs do not establish independence if controlled by the same party.

## Review, remedies, and recovery

Design time-limited mandates, notice/challenge windows, reasoned referrals, bounded dispute pauses, accountable resumption, and prospective migration/upgrades. No automatic approval on silence or timeout. Separate key custody and execution privileges so one operator cannot control law-making, review, and implementation. Specify key loss, rotation, compromise, issuer revocation, recovery and continuity without extra identities/votes.

The constitutional court needs a duly authorized route to suspend or correct unlawful effects; historical records remain auditable. Emergency/upgrade keys need narrow scope, distributed authorization, reasons, expiry, independent review, and safe recovery. No unlimited administrator or irreversible contract can substitute for constitutional control. Distinguish finality of ledger history from continuing validity of a mandate or decision.

Before implementation adopt a threat model, chain/validator governance and resource analysis, security audit, privacy and legal assessment, funding/fee access, accessibility, and non-ledger fallback for outages or exclusion. Test mandate expiry, forged/replayed authorization, duplicated allocations, referral loops, captured oracles, compromised keys, and court-ordered remedies. No tokens, financial products, contract deployment, or external identity integration are authorized by this document.

## Primary technical references and limits

- [Ethereum: smart contracts](https://ethereum.org/developers/docs/smart-contracts/) and [oracles](https://ethereum.org/developers/docs/oracles/): external information requires interfaces outside contract execution; not an endorsement or chain selection.
- [W3C Verifiable Credentials Data Model 2.0, Recommendation 15 May 2025](https://www.w3.org/TR/2025/REC-vc-data-model-2.0-20250515/): candidate attestation vocabulary; trusting an issuer is distinct from cryptographic verification. No implemented conformance is claimed.
- [Douceur, The Sybil Attack, 2002](https://www.microsoft.com/en-us/research/publication/the-sybil-attack/): multiple identities can amplify one controller; certified identity alone does not solve this project's political allocation problem.
