
# JEVLab Research Plan

## Working Title

Evaluating Reasoning and Decision-Making Capabilities
of System One Models: From Text to Simulated Navigation

## 1. Motivation

Modern language models often rely on autoregressive
generation and explicit chain-of-thought prompting
to solve complex reasoning problems.

Jev, developed by TypeSafe AI, is designed for
direct, structured, probabilistic decision-making.

This raises the question of whether fast,
direct-decision models can support tasks involving
multi-step reasoning and sequential decision-making.

Our research investigates these capabilities
across text, visual information, and simulated
navigation environments.

## 2. Main Research Question

Can Jev perform multi-step reasoning and reliable
sequential decision-making without explicitly
generating intermediate reasoning steps?

## 3. Research Phases

### Phase 1: Text Reasoning

Objective:
Evaluate Jev's performance on multi-hop
logical reasoning tasks.

Experiments:
- Controlled relational reasoning datasets
- Different reasoning chain lengths
- Distractor statements
- Direct-answer evaluation
- Comparison with baseline neural models

Metrics:
- Accuracy
- Confidence calibration
- Inference latency
- Generalization to unseen problem structures

### Phase 2: Image-Based Decisions

Objective:
Investigate whether Jev can make reliable
decisions grounded in visual information.

Experiments:
- Object relationship reasoning
- Spatial reasoning
- Visual scene interpretation
- Decision-making based on object positions

A separate perception module may be required
to convert images into structured text states.

Metrics:
- Decision accuracy
- Spatial reasoning accuracy
- Robustness to scene complexity

### Phase 3: Navigation Simulation

Objective:
Evaluate whether repeated direct decisions
can support multi-step tasks in interactive environments.

Simulation:
- Python GridWorld
- MiniGrid
- Optional robotics simulation environments

Pipeline:

Environment
    |
Observation
    |
Structured State
    |
Jev Decision Model
    |
Action Selection
    |
Environment Update
    |
Next Observation

Experiments:
- Goal-reaching tasks
- Obstacle avoidance
- Sequential navigation
- Unseen environment generalization

Metrics:
- Task success rate
- Average episode length
- Invalid action rate
- Decision latency

## 4. Baseline Comparison

Potential baselines include:

- Lightweight Transformer classifier
- Stepwise reasoning language model
- Random decision policy
- Classical planning methods such as BFS or A*

Baselines will be selected based on the task
and compared under controlled conditions.

## 5. Research Hypotheses

H1:
Jev may solve multi-hop reasoning tasks without
explicitly generating a reasoning trace.

H2:
Reasoning accuracy may decrease as the number
of required inference steps increases.

H3:
Repeated direct decisions may support successful
sequential navigation in simple environments.

H4:
The quality of visual state representations may
significantly affect downstream decision performance.

These hypotheses will be evaluated experimentally.

## 6. Current Scope

The NNDL Final Project will primarily focus on
Text Reasoning.

Image-based decision-making and navigation simulation
are planned extensions, depending on API access,
development progress, and available time.

## 7. Current Status

Research planning and experimental design.

No trained models, completed experiments,
or validated performance results are reported yet.
