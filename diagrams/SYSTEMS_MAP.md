---
title: Institutional and Technical Systems Map
tags: [diagrams, mermaid, architecture, MOC]
---
# Systems Map

The diagrams below render as Mermaid in GitHub and Obsidian. Arrows describe **research relationships and accountable processes**, not ecclesial approval or mechanical proof of ethical behavior.

## From source to remedy

~~~mermaid
flowchart TD
  A["Primary CST documents"] --> C["Foundational Principles Charter"]
  B["Author's original economic and civic proposals"] --> C
  C --> D["Project axioms and interpretive method"]
  D --> E["Decision protocol"]
  E --> F["System requirements"]
  F --> G["Benchmark scenarios"]
  G --> H["Human evaluation + dissent"]
  H --> I["Corrective action and verification"]
  I --> F
  J["Rights, law, and freedom of conscience"] --> E
  K["Independent reviewers and affected communities"] --> H
  L["HDPL experimental license"] -. "separate legal track" .-> M["Legal review"]
~~~

## Responsibilities and checks

~~~mermaid
flowchart LR
  Person["Affected person / community"] -->|"questions, corrections, lived expertise"| Owner["Accountable human decision owner"]
  Model["AI decision support"] -->|"evidence, options, uncertainty"| Owner
  Owner -->|"reasoned decisions"| Person
  Person -->|"appeals"| Review["Independent human review"]
  Review -->|"remedy / correction"| Owner
  Auditor["Independent audit"] -->|"findings"| CAPA["Correction and verification"]
  CAPA -->|"tested changes"| Model
  CAPA -->|"governance reports"| Review
  Operator["System operator"] --> Model
  Auditor -. "checks" .-> Operator
~~~

## Federation analogy

~~~mermaid
flowchart TD
  E1["Worker-owned enterprise A"] --> F["Federation congress (bounded mandate)"]
  E2["Worker-owned enterprise B"] --> F
  E3["Worker-owned enterprise C"] --> F
  F --> S["Delegated services cooperative"]
  F --> I["Worker-owner education institute"]
  F --> D["Development fund"]
  S -. "service, not ownership" .-> E1
  S -. "service, not ownership" .-> E2
  S -. "service, not ownership" .-> E3
  A["Independent audit / protected dissent"] -. "reviews" .-> F
~~~

**Interpretive note:** No diagram alone resolves allocation of rights, security, funding or institutional competence. See [[business/LEON13_AI_FEDERATION|applied federation]] and [[ai/ARCHITECTURE|architecture]].
