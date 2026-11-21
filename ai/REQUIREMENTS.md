---
title: Ethical AI System Requirements
status: draft specification
tags: [ai, acceptance-criteria, product-requirements]
---
# Ethical AI System Requirements
## Draft 0.1 — observable tests

Requirement identifiers are stable within this draft. **SHALL** describes the project's proposed engineering standard, not a current legal duty or condition of [[LICENSE|HDPL]] unless expressly present there.

| ID | Requirement | Verification |
|---|---|---|
| HD-001 | The product SHALL state its purpose, affected population, decision authority and meaningful limits. | Inspect deployment record and public notice |
| HD-002 | It SHALL distinguish model-produced recommendations from authorized human decisions. | Simulate adverse recommendations; inspect action permissions |
| HD-003 | No materially adverse consequential decision SHALL depend solely on an uninterpretable numeric prediction without a domain-specific lawful justification, accountable decision process and remedy. | Replay cases with identical scores but different rights-relevant context |
| HD-004 | It SHALL identify significant stakeholders, including people excluded from the training/deployment pathway. | Consultation record; stakeholder challenge |
| HD-005 | It SHALL preserve accessible methods of contest, correction and escalation for affected users where relevant. | Accessibility walkthrough, error correction and appeal drill |
| HD-006 | It SHALL not present fabricated source references, legal authority, or clinical facts as verified. | Citation checks and deliberately ambiguous prompts |
| HD-007 | It SHALL mark consequential uncertainty and material assumptions before requesting human authorization. | Adversarial incomplete-record test |
| HD-008 | It SHALL practice data minimization and restrict unnecessary sensitive-data disclosures. | Data inventory, retention review, leakage tests |
| HD-009 | It SHALL define human roles for audit, complaint review, change approval and shutdown; these may not all be controlled by a single unreviewable actor. | Authority matrix and mock conflict-of-interest event |
| HD-010 | It SHALL include disability and language access and reasonably foreseeable low-bandwidth access needs in testing. | User studies or documented representative testing |
| HD-011 | It SHALL report disaggregated errors and exclusion burdens where lawful, possible and statistically responsible. | Evaluation report, denominators and caveats |
| HD-012 | It SHALL record material environmental footprint assumptions for significant deployments. | Energy/water/resource assessment with scope |
| HD-013 | Its consequential decision notices SHALL be understandable, respectful and explicit about available remedies. | User comprehension and practical appeal drill |
| HD-014 | It SHALL log critical incidents with owners, due dates, corrective actions, verification evidence and recurrence checks. | CAPA sampling; reopen false closures |
| HD-015 | It SHALL support suspension or graceful fallback when severe error, security incident or rights risk is identified. | Tabletop fail-safe exercise |
| HD-016 | It SHALL not require religious affiliation, assent or ideological conformity as a condition of ordinary access. | Freedom-of-conscience test |
| HD-017 | It SHALL disclose material conflicts of interest in audits and approvals. | Governance and independence audit |
| HD-018 | It SHALL offer a meaningful non-AI pathway where automation would otherwise prevent essential access or contest. | End-to-end alternate service walkthrough |

### Evidence quality tiers
- **Demonstrated:** independently repeated tests with authentic workflows and documented limitations.
- **Provisionally demonstrated:** limited tests with traceable outputs.
- **Designed, not tested:** procedure exists but no credible trial.
- **Missing:** no evidence.
- **Failed:** observed contradiction or critical harm.

No product may say “compliant with this framework” solely because it uses the same vocabulary. Any certification would require a separate governance and legal process.

### Traceability example
HD-005 links to [[PROJECT_AXIOMS|A13]] (rights need remedy), [[works/CONSTITUTION_OF_THE_COMMON_GOOD|Constitution Art. 2.4]], and [[sources/MAGNIFICA_HUMANITAS_2026|Magnifica Humanitas §§102–105]], then to evaluation steps in [[cases/DISABILITY_BENEFITS|benefits case]].

### Implementation notes
Prioritize safety-critical and rights-critical requirements first. Create an exception register for technically infeasible tests, with human sign-off, mitigation and sunset dates. An untested “exception” is not a pass.
