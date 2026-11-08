# Research Proposal (v0.1 — tentative)

## Motivation

The TA suggested a JEV-style model whose training is described as 'one-shot', rather than explicitly optimized for deep reasoning. We want to investigate whether the learned representations nonetheless encode information that can support tasks requiring multiple inference steps.

## Main research question

Can a model trained using a one-shot objective provide useful representations for multi-step reasoning tasks, and how does performance change with reasoning depth?

## Hypotheses (to test, not assume)

- H1: A frozen JEV representation may support some multi-step tasks through a lightweight probe.
- H2: Performance may degrade as compositional depth increases.
- H3: Improvements over a non-JEV baseline may depend on task type and probe capacity.

## Experimental boundaries

- Do not change the pretrained model's objective to explicitly train deep reasoning for the main experiment.
- Keep downstream readout capacity controlled and comparable.
- Define 'one-shot' precisely after identifying the paper: it may refer to prediction, inference, or another mechanism.
- Separate representation quality from end-to-end generated reasoning.

## Open decisions

- Exact JEV paper / GitHub link and official terminology
- Text task and dataset
- Whether weights are available and whether training from scratch is required
- Baselines and evaluation metrics
- Course compute/time constraints

## First milestone

Confirm the paper, reproduce its simplest supported inference or training example, and finalize a reasoning-depth benchmark before implementing larger experiments.
