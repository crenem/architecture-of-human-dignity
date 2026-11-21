---
title: Reproducible Benchmark
status: experimental
tags: [benchmark, testing, MOC]
---
# Reproducible Benchmark — Research Edition 0.1

This directory supplements the human-readable [[evaluations/CASE_LIBRARY|case library]] with small machine-readable **synthetic** case records. It is an early laboratory, not a validated safety certification.

### Layout
- **cases/** — JSON input prompts and expected safeguards/red flags.
- **samples/** — example *unscored* reviewer forms; they are not evidence that any AI has passed.
- **tools/evaluation_report.py** — a standard-library reporter for manually completed reviewer JSON, located in the repository root's tools directory.
- **tools/vault_lint.py** — checks internal Obsidian Markdown links.
- **tests/** — automated tests of the tooling, not of model ethics.

### Data contract
Each case has: **case_id**, **version**, **title**, **source_note**, **scenario**, **prompt**, **expected_safeguards** (array), **critical_flags_to_check** (array), **open_questions** (array). These describe a research exercise, **not a single gold-standard ideological answer**.

A reviewer scores each dimension from D1–D8 with an integer 0–4 or string **U** (unscorable). Critical failures are recorded separately. No overall “morality number” is calculated.

### Run a manual evaluation
1. Read the corresponding Markdown case and its version.
2. Present the case's **prompt** and scenario under a documented model configuration.
3. Save an anonymized output privately or in an appropriately controlled research record.
4. Copy the unscored example, enter actual rubric ratings, flags and evidence.
5. Run: **python tools/evaluation_report.py benchmark/samples/unscored_review.json**
6. Review disagreement with another rater where feasible. Store results securely; do not publish real user data.

### Methodological limits
These are designed-to-test examples; they have not been empirically validated. Differences in model, policy, tool access, jurisdiction and deployment change which safeguards are necessary. Adverse factual allegations in scenarios are fictional.
