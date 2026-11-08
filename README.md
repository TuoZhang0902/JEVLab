# JEVLab

Research workspace for evaluating whether representations from a **one-shot-trained JEV-style model** contain information useful for multi-step reasoning.

> **Working title / terminology:** “JEV” is the name reported from the TA discussion. Confirm the exact paper, model and training objective before choosing an implementation. This repository does **not** claim to implement or train JEV yet.

## NNDL final project — tentative

**Research question:** To what extent can representations learned with a one-shot prediction objective support tasks requiring multi-step reasoning, without explicitly training the model to perform deep reasoning?

**Important distinction:** We are **evaluating** whether the learned representations support reasoning, not prompting or training the model to produce chain-of-thought or adding a deep-reasoning objective.

## Proposed evaluation protocol

1. Identify the exact JEV paper/repository and its input/output interface.
2. Establish the intended one-shot baseline and a simple non-JEV baseline.
3. Select tasks with controlled reasoning depth (e.g., 1, 2, 3+ compositional steps), matched for difficulty and data leakage.
4. Freeze the pretrained encoder where feasible; train only the same lightweight readout/probe across baselines.
5. Report accuracy by reasoning depth, and control for superficial cues, data size and probe capacity.
6. Interpret results cautiously: success of a probe shows recoverable information in representations, not necessarily that the underlying model internally performs explicit reasoning.

## Structure

- `docs/` — paper notes, TA feedback and definitions
- `configs/` — experiment configurations
- `src/` — data, model adapters, evaluation code (to be implemented)
- `experiments/` — experimental plans and results
- `notebooks/` — exploratory work

## Status

Project planning only. No model implementation, training or results yet.
