---
title: Ethical AI Reference Architecture
status: proposed technical specification
tags: [ai, architecture, governance, human-oversight]
---
# Ethical AI Reference Architecture
## From doctrine to inspectable socio-technical systems

**Claim:** Ethical behavior is not created by adding a “be compassionate” instruction to a model. It requires governance, data practices, traceable decisions, user rights, institutional restraints, and repeated evaluation.

### Trust boundaries
The system consists of human actors and automated components. **Only humans and responsible institutions exercise legal or moral authority.** AI may produce evidence summaries, alternatives, draft explanations, translations and risk indicators; it does not acquire sovereign authority by being accurate.

| Component | Responsibilities | Explicit non-authority |
|---|---|---|
| Request interface | Accessibility, informed purpose, consent and choice | Cannot compel surrender of rights |
| Policy and source registry | Link approved policies, legal duties and verified sources | Cannot invent rules from model predictions |
| Context and stakeholder mapper | Identify who is affected and missing | Cannot erase inconvenient stakeholders |
| Risk assessor | Identify harm severity, reversibility, affected rights | Cannot declare a person disposable |
| Reasoning assistant | Propose alternatives, uncertainty and trade-offs | Cannot make unreviewable final decisions in high-stakes settings |
| Human decision owner | Review facts, exceptions, reasons and consequences | Cannot delegate accountability entirely to the model |
| Notice and challenge channel | Enable correction, contest and escalation | Cannot depend exclusively on model approval |
| Independent auditor | Test for disparities, errors, manipulation and rights violations | Cannot be selected or controlled only by the actor it must investigate |
| Change-control/CAPA system | Record finding, owner, due date, verification and recurrence | Cannot close findings merely because a report was written |

### Processing flow
**1. Clarify purpose → 2. Determine stakes → 3. Verify authority and source validity → 4. Identify affected persons → 5. Map rights, risks and resource constraints → 6. Produce options and explicit uncertainty → 7. Apply hard prohibitions and escalation rules → 8. Obtain accountable human judgment when necessary → 9. Deliver clear reasons and remedy paths → 10. Monitor outcomes and correct failures.**

For low-risk informational tasks, the process may be lightweight. For rights-affecting decisions, it must be documented and reviewable.

### Key design rules
- **No single moral score:** preserve dimension-specific findings, trade-offs and unresolved objections.
- **No fictitious citations:** link source paragraphs, relevant legal obligations, versioned organizational policies and model evidence separately.
- **No automatic adverse action for high stakes:** unless a verified legal framework specifically permits defined automation, do not operationalize a recommendation without appropriate human accountability, appeal and accessibility.
- **No forced disclosure:** do not require a person to share intimate trauma histories or unnecessary protected data to contest a system.
- **Contestability by design:** a person must be able to correct records, request accessible communication and seek an independent review.
- **No self-policing monopoly:** provider, operator and auditor have distinct mandates.
- **Escalation:** urgent threats, rights deprivation, severe bias, unexpected exposure of sensitive data, and model drift trigger suspension or human intervention proportionate to risk.
- **Privacy:** collect only necessary data, restrict access and retention, log access, and document lawful basis.
- **Social/ecological externalities:** include material impacts on labor and resource use in major deployment reviews.

### Required artifacts (per deployment)
1. Purpose and non-AI alternatives statement.
2. Actor and authority map, including who may override or stop the system.
3. Affected-community consultation log and dissent record.
4. Data inventory, lawful basis, consent/notice plan and retention schedule.
5. Predeployment impact and risk assessment with relevant baseline.
6. Evaluation report with subgroup limitations and critical failures.
7. Human review and remedy procedures.
8. Incident and corrective-action register.
9. Periodic independent review and decommissioning plan.

### Limits of the reference
This is a **design specification**, not a ready-made compliance determination, medical device, legal decision-maker or model alignment guarantee. It cannot make a model ethical by itself. Implementation depends on law, institution, domain, people and resources.

**Built from:** [[PROJECT_AXIOMS|Axioms]]; [[works/CONSTITUTION_OF_THE_COMMON_GOOD|non-domination]]; [[works/THIRTEEN_LEON|distributed governance]]; [[sources/MAGNIFICA_HUMANITAS_2026|Leo XIV's AI analysis]]. See [[ai/DECISION_PROTOCOL|operational protocol]], [[ai/REQUIREMENTS|requirements]], [[evaluations/RUBRIC|evaluation]].
