# JEVLab — Extra Tokens and Evidence-Sensitive Reasoning

A Columbia University COMS W4776 research project studying whether additional token positions improve reliable composition of information, first in text and then in matched visual problems.

**Status: research planning and collaboration setup.** This repository contains documentation, provisional dependencies, and placeholder directories. Benchmarks, model adapters, training, and evaluation are not implemented; no experimental results are claimed.

## Motivation and research question

Can additional computational tokens improve reasoning without providing additional problem-specific information? Repeated punctuation adds input positions, but also changes formatting, attention, and response preferences. Accuracy gains alone do not establish better reasoning or extra sequential computational depth.

> Do filler tokens improve reliable compositional reasoning and evidence sensitivity, rather than merely changing prompt-response behavior?

We test whether models respond correctly when relevant evidence changes and remain correct when irrelevant evidence changes. Negative and inconclusive findings are valid outcomes.

## Three research stages

| Stage | Intended experiment | Scope |
| --- | --- | --- |
| **Text reasoning** | Controlled multi-hop graph traversal, filler-token interventions, and counterfactual evidence changes | Core deliverable |
| **Visual reasoning** | Equivalent graph/query instances represented as images, using the same checkpoint and fixed intervention | Planned extension, gated by perception and compute feasibility |
| **Robot decision-making** | Test whether reliable evidence use transfers to sequential decisions in simulated navigation | Stretch goal; no physical robot or full VLA training |

JEVLab retains its name and the teammate's text → vision → navigation roadmap. Jev, JEPA, and any particular architecture are **not requirements**. The [current proposal](docs/research_proposal.md#relationship-to-earlier-work) explains the move from a Jev-specific capability study to controlled token interventions. The [earlier proposal](docs/history/2026-11-09-system-one-proposal.md) is preserved verbatim as historical context, not the active specification.

## Proposed methodology

- Generate deterministic directed graphs with relation-labelled edges and queries requiring 1, 2, or 4 compositional steps.
- Pair each original with a relevant edit that changes its answer and a matched irrelevant edit that preserves it.
- Compare no filler, exact-token-count punctuation fillers, identity/placement controls, and explicit predicted intermediate nodes.
- Fix checkpoint, graph family, choices, prompt template, and scoring within comparisons; use separate development and confirmatory families.
- Keep all related edits and renderings together when splitting data, and check for duplicates and superficial answer cues.

The primary hypothesis is that a fixed post-problem filler intervention improves **answer-changing pair correctness**: both original and edited answers must be correct. Secondary hypotheses concern placement dependence and robustness to irrelevant changes. Visual and navigation hypotheses are evaluated only after their gates pass.

Report ordinary accuracy, pair correctness, robustness by depth, invalid outputs, latency, token counts, and peak memory. Estimate paired uncertainty by resampling graph families. Invariant wrong predictions are not evidence sensitivity. Equal token counts do not imply equal compute across prefill, generated reasoning, and vision processing.

Fixed prompt fillers are the core intervention. Forced decoding of an identical sequence is an implementation equivalence check, not a separate reasoning mechanism. Model-selected filler tokens can encode information. Learned static embeddings and recurrent latent thoughts require separate training-matched designs and are outside the minimum experiment.

Read the [research specification](docs/research_proposal.md) for hypotheses, controls, and metrics, and the [roadmap](docs/roadmap.md) for milestones, tests, and resource gates.

## Models and next milestones

Candidate open-weight models are Qwen2.5-VL-3B-Instruct (default candidate for text and vision), SmolLM2-1.7B-Instruct (text fallback/replication), and SmolVLM2-2.2B-Instruct (smaller multimodal alternative). Select by competence, exact scoring access, and resources—not the largest filler gain.

1. Confirm current course requirements, hardware allocation, protocol, and team responsibilities.
2. After implementation approval, validate the graph generator and counterfactual edits.
3. Validate token insertion/scoring and run a bounded text pilot.
4. Freeze the confirmatory protocol, complete the text study, and report all outcomes.
5. Apply the vision gate; consider navigation only after the core is complete.

Training is not scientifically required for the inference-only question; whether the current course rubric requires it remains unverified. The existing unpinned `requirements.txt` is a provisional package list, not a validated environment. No setup or experiment command is claimed to work yet.

## Repository structure

```text
JEVLab/
├── README.md
├── docs/
│   ├── research_proposal.md     # Current specification
│   ├── roadmap.md               # Milestones, tests, and decision gates
│   └── history/
│       └── 2026-11-09-system-one-proposal.md
├── configs/                     # Placeholder for future configurations
├── src/                         # Placeholder for future experiment code
├── experiments/                 # Placeholder for future records/results
├── notebooks/                   # Placeholder for exploratory analysis
├── requirements.txt             # Provisional, unvalidated dependencies
└── .gitignore
```

## Collaboration

Use focused branches and pull requests against `main`. Check upstream and local changes before editing; never force-push or overwrite a teammate's work. Separate documentation changes from experiment implementation. Each experiment PR should state its hypothesis, changes, commands/checks, resource use, and limitations. Document direction changes and preserve proposal history.

Keep credentials, weights, and large datasets out of Git. Preserve compact configurations, manifests, and predictions in tracked paths or documented artifact storage; check `.gitignore` before relying on output directories. Pin model/environment revisions when implementation begins. Planned work must never be reported as completed work.

## Selected literature

These papers establish prior art and methodological context, not results for JEVLab.

- Goyal et al., [Think before you speak: Training Language Models With Pause Tokens](https://arxiv.org/abs/2310.02226) — trained pause-token computation.
- Pfau et al., [Let's Think Dot by Dot: Hidden Computation in Transformer Language Models](https://arxiv.org/abs/2404.15758) — filler computation on trained algorithmic tasks.
- Jang et al., [Expanding Computation Spaces of LLMs at Inference Time](https://arxiv.org/abs/2509.24884) — inference-only identity, count, and placement effects.
- Hao et al., [Training Large Language Models to Reason in a Continuous Latent Space](https://arxiv.org/abs/2412.06769) — Coconut's recurrent continuous thoughts, distinct from fixed fillers.
- Ray et al., [Mull-Tokens: Modality-Agnostic Latent Thinking](https://arxiv.org/abs/2512.10941) — learned multimodal latent tokens.
- Zhang et al., [Ablate-to-Validate: Are Vision-Language Models Really Using Continuous Thought Tokens?](https://arxiv.org/abs/2605.21642) — token-content utilization diagnostics.
- Baherwani et al., [Not All LLM Reasoning is Visible in the Chain-of-Thought](https://arxiv.org/abs/2607.22925) — synthetic filler studies and mechanistic diagnostics.
- Sun et al., [GraphVerse](https://arxiv.org/abs/2608.06769), and Xue et al., [TwinICL](https://arxiv.org/abs/2609.15028) — visual graph and paired-modality evaluation.
- Bai et al., [Latent Reasoning VLA](https://proceedings.mlr.press/v306/bai26h.html) — embodied context, not a required baseline.

## Team

Tuo Zhang and Charles Gao · Columbia University · COMS W4776, Neural Networks and Deep Learning · Fall 2026
