# ReasonSpace

**Do latent slots track an agent's position across four moves?**

Columbia University · COMS W4776: Neural Networks and Deep Learning

An agent takes four moves on a visual grid. We will train two versions of Qwen2.5-VL-3B-Instruct to predict its final cell. Both models have one learned slot after each move. L1 learns from the final answer. L2 also learns to predict the visual state after each move.

The simulator lets us test a specific prediction. If we replace the second slot with one from a different halfway position, does the model assign more probability to the destination reachable from that position? An off-path wall edit gives us a control that preserves the halfway position.

## Project materials

**Planning stage, updated November 19, 2026.** The roadmap starts with a visual perception check and a short training pilot. The primary experiment is a matched L1/L2 comparison on four-step visual routes.

- [Two-page course proposal](docs/proposal/reasonspace_proposal.pdf)
- [Research specification and decision rules](docs/research_proposal.md)
- [Milestones and provisional GPU budget](docs/roadmap.md)
- [LaTeX source ZIP](docs/proposal/reasonspace_source.zip)

## Selected literature

- [Think before you speak: Pause Tokens](https://arxiv.org/abs/2310.02226) · [Let's Think Dot by Dot](https://arxiv.org/abs/2404.15758) · [Expanding Computation Spaces at Inference Time](https://arxiv.org/abs/2509.24884)
- [Fast-ThinkAct (CVPR 2026)](https://arxiv.org/abs/2601.09708) · [LaRA-VLA (ICML 2026)](https://arxiv.org/abs/2602.01166)
- [Ablate-to-Validate](https://arxiv.org/abs/2605.21642) · [WM-VLM](https://arxiv.org/abs/2609.34826)

**Team:** Charles Gao, Tuo Zhang, and Jiahao Zhang
