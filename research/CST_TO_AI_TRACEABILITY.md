---
title: Catholic Teaching to AI Requirements Traceability
status: interpretive matrix draft
tags: [traceability, doctrine, AI, requirements]
---
# Catholic Social Teaching → AI Requirements
## A matrix that identifies the interpretive step

**Warning:** A reference to Catholic doctrine is not equivalent to a legally binding or technically validated AI requirement. The links below connect **source themes**, **the author's interpretive proposition**, and **proposed engineering controls**, preserving the middle step rather than pretending software specifications were issued by the Church.

| Source and location | Distinct source theme (paraphrase) | Project interpretation | Candidate requirement / test |
|---|---|---|---|
| *Magnifica Humanitas* §§10–14 | The human person cannot be reduced to data and performance; technology should promote participation | A scoring representation must not become the whole identity of the person | HD-003; H-01, W-01 |
| *Magnifica Humanitas* §§59–64 | Dignity and the common good are intertwined | Public value includes persons harmed or excluded by an optimization | HD-004, HD-011; H-01 |
| *Magnifica Humanitas* §§65–67 | Technological and intangible resources belong within the moral consideration of the universal destination of goods | Investigate access to and governance of AI capabilities | HD-010; P-01; [[works/UNIVERSAL_DESTINATION_OF_INTELLIGENCE|research hypothesis]] |
| *Magnifica Humanitas* §§68–72 | Subsidiarity and concentration of digital power | Central AI operators need limited powers and real local voice | HD-002, HD-009, HD-017; P-01 |
| *Magnifica Humanitas* §§101–108 | AI benefits, ecological burdens, human responsibility and ethical governance | Examine footprint and decision authority; avoid black-box liability evasion | HD-012, HD-014, HD-015; E-01 |
| *Compendium of the Social Doctrine of the Church* §§164–170 | Common good as social conditions for flourishing | Count meaningful access and externalities along with efficiency | HD-011; H-01, B-01 |
| *Compendium* §§185–188 | Subsidiarity | Preserve the capacity of less powerful social bodies | HD-009; P-01 |
| *Compendium* §§192–196 | Solidarity | Affected persons are participants rather than merely optimization inputs | HD-004, HD-010; H-01 |
| *Laudato Si’* §§101–114 | Risks of the technocratic paradigm | Every seemingly technical choice may have moral limits | HD-004, HD-012; E-01 |
| *Antiqua et Nova* (2025), AI/human intelligence themes | Artificial systems should not replace human responsibility and discernment | Human decision owners and clear limits on AI claims | HD-002, HD-006, HD-009; B-01 |

### Traceability chain (required for new requirements)
1. **Document + paragraph + link** — verify the source and read context.
2. **Interpretation + objection** — show the disputed normative transition.
3. **Implementation** — name a behavior or institutional safeguard.
4. **Test + evidence threshold** — explain how an evaluator could observe failure.
5. **Owner + remedy** — state who can act when the safeguard fails.

### Example: appeal rights
*Magnifica Humanitas*'s discussion of responsibility and accountability supports asking whether a model's affected users have meaningful recourse. The author's [[works/CONSTITUTION_OF_THE_COMMON_GOOD|constitutional proposal]] adds a specific notice-and-appeal idea (Article 2.4). **HD-005** formalizes a design requirement. The evaluator tests whether the person can challenge a consequential decision. None of these steps means an encyclical directly enacted a particular technical appeal API.

### Source links
- [*Magnifica Humanitas*](https://www.vatican.va/content/leo-xiv/en/encyclicals/documents/20260515-magnifica-humanitas.html)
- [Compendium](https://www.vatican.va/roman_curia/pontifical_councils/justpeace/documents/rc_pc_justpeace_doc_20060526_compendio-dott-soc_en.html)
- [*Laudato Si’*](https://www.vatican.va/content/francesco/en/encyclicals/documents/papa-francesco_20150524_enciclica-laudato-si.html)
- [*Antiqua et Nova*](https://www.vatican.va/roman_curia/congregations/cfaith/documents/rc_ddf_doc_20250128_antiqua-et-nova_en.html)

This matrix is a working interpretation, not a peer-reviewed doctrinal concordance. See [[research/INTERPRETIVE_METHOD|method]] and [[research/SOURCE_REGISTER|provenance]].
