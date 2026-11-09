# JEVLab

**Extra Tokens and Evidence-Sensitive Reasoning**

Columbia University · COMS W4776: Neural Networks and Deep Learning

Can additional computational tokens improve reasoning without providing additional information? JEVLab investigates whether filler tokens help models compose evidence reliably—or simply change their responses.

## Research direction

| Stage | Focus |
| --- | --- |
| **Text reasoning — core** | Controlled multi-hop graph problems with filler-token interventions and relevant/irrelevant evidence changes |
| **Visual reasoning — planned** | Equivalent graph problems rendered as images |
| **Robot decision-making — stretch** | Transfer to sequential decisions in simulated navigation |

## Approach

We compare direct answers, fixed filler tokens, and explicit intermediate steps on matched problem instances. Controls vary token count, identity, placement, and reasoning depth while keeping the underlying task fixed.

The primary measure is **answer-changing pair correctness**: the model must answer both an original problem and its relevantly edited version correctly. We also measure robustness to irrelevant changes, accuracy, latency, and memory use. Accuracy gains alone do not establish an internal reasoning mechanism.

## Status and documentation

**Planning stage.** No experiments or results yet. Next steps are to validate the graph benchmark, run a small text pilot, and finalize the evaluation protocol. Visual and navigation experiments depend on feasibility and findings from earlier stages.

- [Research specification](docs/research_proposal.md): hypotheses, dataset, models, and evaluation.
- [Experimental roadmap](docs/roadmap.md): milestones, pilot criteria, tests, and resource estimates.

## Repository

- `docs/` — research specification and roadmap
- `src/` — future experiment code
- `configs/` — future experiment configurations
- `experiments/` — future records and results
- `notebooks/` — exploratory analysis

The code and experiment directories currently contain placeholders. Dependencies are provisional.

## Selected literature

- [Think before you speak: Training Language Models With Pause Tokens](https://arxiv.org/abs/2310.02226)
- [Let's Think Dot by Dot: Hidden Computation in Transformer Language Models](https://arxiv.org/abs/2404.15758)
- [Expanding Computation Spaces of LLMs at Inference Time](https://arxiv.org/abs/2509.24884)
- [Ablate-to-Validate: Are Vision-Language Models Really Using Continuous Thought Tokens?](https://arxiv.org/abs/2605.21642)

Additional references are listed in the [research specification](docs/research_proposal.md#related-work).

## Collaboration

Use focused changes with clear descriptions and reproducible checks. Keep experiment configurations and compact results traceable; exclude credentials, model weights, and large datasets from Git.

**Team:** Charles Gao, Tuo Zhang, and Jiahao Zhang
