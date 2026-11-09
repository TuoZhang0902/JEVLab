# JEVLab

Exploring reasoning and decision-making capabilities of
System One AI models across text, vision, and simulated
robotic environments.

## Overview

JEVLab is a research-oriented project investigating
whether Jev, a System One decision model developed by
TypeSafe AI, can perform complex reasoning and
sequential decision-making without explicitly generating
intermediate reasoning steps.

The project begins as a final project for COMS W4776
Neural Networks and Deep Learning at Columbia University,
with the goal of supporting further research.

## Research Objective

Our central research question is:

**Can a System One model support multi-step reasoning
and reliable decision-making across increasingly complex
tasks without explicit chain-of-thought generation?**

We investigate this question through three stages:

1. Text-based reasoning
2. Image-based decision-making
3. Navigation and robotic simulation

## Research Roadmap

### Phase 1: Text Reasoning

Evaluate Jev on logical and multi-hop reasoning tasks.

Research questions:
- Can Jev solve multi-step reasoning problems?
- How does reasoning depth affect accuracy?
- How well calibrated are its decisions?
- How does its performance compare with neural baselines?

Planned experiments:
- Relational reasoning
- Multi-hop logical inference
- Reasoning depth analysis
- Accuracy and confidence evaluation
- Comparison with baseline models

### Phase 2: Image-Based Decision-Making

Investigate whether Jev can support decisions
based on visual information.

Planned experiments:
- Object and spatial relationship reasoning
- Scene understanding
- Visual question answering
- Structured decisions from visual observations

If native image input is unsupported, visual information
will be converted into structured representations
using a separate perception module.

### Phase 3: Navigation and Robotic Simulation

Explore whether Jev can support sequential
decision-making in simulated environments.

Initial environments:
- Python GridWorld
- MiniGrid
- Optional robotics simulators

Planned tasks:
- Goal-directed navigation
- Obstacle avoidance
- Sequential action selection
- Decision-making under changing environments

Jev will act as a high-level decision-making component.
The simulation environment will execute selected actions.

No physical robot is required for the initial experiments.

## Proposed Evaluation Metrics

### Text Reasoning
- Accuracy
- Reasoning depth
- Confidence calibration
- Inference latency

### Image-Based Decisions
- Decision accuracy
- Spatial reasoning performance
- Robustness to visual complexity

### Navigation Simulation
- Task success rate
- Average steps to completion
- Invalid action rate
- Decision latency
- Generalization to unseen environments

## Repository Structure

```text
JEVLab/
├── configs/
├── docs/
│   └── research_proposal.md
├── experiments/
│   ├── text/
│   ├── image/
│   └── navigation/
├── notebooks/
├── src/
│   ├── adapters/
│   ├── data/
│   ├── models/
│   ├── evaluation/
│   └── simulation/
├── .gitignore
├── README.md
└── requirements.txt
```

## Project Status

**Current Stage: Research Planning**

- [ ] Confirm Jev API access and capabilities
- [ ] Develop text reasoning benchmark
- [ ] Implement baseline models
- [ ] Evaluate Jev on text reasoning tasks
- [ ] Develop image-based decision experiments
- [ ] Implement navigation simulation
- [ ] Compare decision-making performance

The current repository contains the research framework.
No experimental results are claimed yet.

## Future Directions

- Multimodal decision-making
- Sequential planning
- Embodied AI
- Robotic task planning
- Decision-making under uncertainty

## Authors

Tuo Zhang and Charles

Columbia University
COMS W4776 — Neural Networks and Deep Learning
Fall 2026
