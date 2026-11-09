# Research specification: extra tokens and evidence sensitivity

Updated 2026-11-09. **Planning specification; experiments are not implemented.** Numerical settings are proposed defaults to approve before coding. [Roadmap](roadmap.md) · [Overview](../README.md)

## Relationship to earlier work

The initial proposal studied frozen representations from an unresolved “one-shot JEV” model. The teammate's subsequent roadmap expanded a Jev capability study to text, images, and simulated navigation. Its three-stage progression, controlled depth, and cautious reporting remain central.

The [proposal at commit 1159387](history/2026-11-09-system-one-proposal.md) is retained verbatim. The current direction changes the central experiment to controlled filler-token interventions because exact token IDs, logits, and model access support stronger comparisons than an unspecified training objective or opaque decision API. Jev may later be a behavioral comparator; neither Jev nor JEPA is required. General scene understanding and large robotics simulators are deferred to keep the course project focused.

## Question and interpretation

Do additional token positions improve reliable compositional reasoning and evidence sensitivity, or merely change response behavior? Does a fixed intervention generalize to equivalent visual graphs and eventually sequential decisions?

The contribution sought is a controlled interaction between token intervention, compositional depth, and relevant/irrelevant evidence edits. Filler gains, token replacement, graph benchmarks, and matched modalities have prior art; no first-ever or mechanistic novelty claim is made. Behavioral reliability does not prove an internal algorithm, and graph hops need not equal internal sequential steps.

## Hypotheses and decision rules

| Hypothesis | Prespecified test |
| --- | --- |
| H1: Post-problem fillers improve reliable composition | 64 dot tokens versus no filler on answer-changing pair correctness, equally weighted across depths 2 and 4 |
| H2: Effects depend on evidence-relative placement | 64 post-problem versus 64 pre-problem dot tokens |
| H3: Improvements survive nuisance changes | Answer-preserving pair correctness, fact reordering, and consistent node renaming |
| H4: The intervention generalizes to visual presentation | Fixed intervention on matched image/text instances in the same checkpoint |
| H5: Reliable evidence use improves sequential decisions | Paired navigation success and action regret; stretch only |

For H1, the proposed practical threshold is +5 percentage points. A 95% confidence interval above zero supports a positive effect; above +5 supports a meaningful effect. An upper bound below +5 rules out that prespecified benefit at the achieved precision. Boundary-crossing intervals are inconclusive. Negative results do not fail the project.

## Canonical dataset

- Twelve nodes, two directed relation types; each relation is a permutation with one incoming/outgoing edge per node.
- Queries specify a start and relation sequence at depths 1, 2, and 4. Deterministic traversal supplies the endpoint. Reject repeated nodes on the queried trajectory initially.
- Present shuffled edge lists with neutral labels and explicit definitions.
- Each family contains original, relevant-edit, and irrelevant-edit instances. Two-edge target swaps within a relation preserve degrees/edge count. Independently verify the relevant edit changes the endpoint and the irrelevant edit preserves it.
- Four fixed choices within a family contain both original/edited endpoints and two distractors. Randomize option order across families and balance correct positions.
- Keep graph size fixed across depth. Record query length separately and use matched-length diagnostics without claiming to remove all difficulty confounds.
- Match edited prompt token lengths where possible; apply fact reordering and consistent renaming on a secondary subset.
- Split by base graph/query family, keeping edits/renderings together. Check exact and relabeling-equivalent duplicates. Use separate development and confirmation seeds.

The solver must attain 100%. A generator or edit-validation failure blocks model evaluation.

## Interventions and baselines

| ID | Condition |
| --- | --- |
| C0 | No filler |
| C1 | 16 post-problem dot tokens |
| C2 | 64 post-problem dot tokens; fixed primary treatment |
| C3 | 64 post-problem comma tokens |
| C4 | 64 pre-problem dot tokens |
| C5 | 64 post-problem tokens from a fixed punctuation mixture |
| C6 | Predicted intermediate-node sequence, capped at 64 generated tokens |

Post-problem means after graph, query, and choices, immediately before the answer cue. Keep other content and the chat template fixed. Insert exact ordinary vocabulary IDs; reject special/control tokens and save IDs plus decoded text. Direct ID insertion may differ from typed punctuation.

Include chance/majority-choice baselines and the exact solver. Oracle intermediate states are diagnostic ceilings, not compute-only baselines. Record C6 transition validity, truncation, and actual cost rather than assuming equal compute.

### Fixed, generated, and learned tokens

Forced cached decoding of the identical sequence should match prefill within numerical tolerance when tokens, masks, positions, and model mode match. This is an integration check, not an independent reasoning mechanism. Model-selected fillers can encode information and are excluded from the core.

Static learned embeddings and recurrent hidden-state feedback are different interventions; neither is required. If training is approved, compare no-slot/fixed-slot conditions with matched data, optimizer, adapter capacity, and updates across three seeds, reporting different compute. Learned slots require another matched condition. Replacement tests can induce distribution shift and do not alone establish reasoning.

## Scoring and analysis

For C0–C5, score four answer labels from logits at a fixed answer position; verify each is one token in that exact context. Audit unconstrained greedy generation on a subset and freeze scoring before confirmation.

**Primary metric:** fraction of families with both original and relevant-edited answers correct. Estimate paired C2 minus C0, equally weighting depths 2 and 4. Do not change the primary contrast based on pilot gains.

Secondary outcomes: accuracy per variant, answer-preserving pair correctness, prediction invariance, correctness transitions after edits, depth/template effects, C6 transition accuracy, invalid outputs, latency, tokens, and peak memory. Invariance alone rewards constant wrong answers and is insufficient.

Bootstrap base families, stratified by depth, using 10,000 resamples. Preserve pairing. Apply Holm correction to families of secondary significance tests; label exploratory analyses. Deterministic reruns are not independent samples.

Plan initially for 400 families per depth. Use pilot discordance to fix 400–800 per depth before opening confirmation data. Target 80% power for a five-point paired effect where affordable; otherwise report achievable precision. Approximate planning: n ≈ (1.96 + 0.84)² q / 0.05², with q the discordant-outcome rate; respect the actual stratified design.

## Models and training decision

Default candidate: [Qwen2.5-VL-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct), supporting text and images in one checkpoint. Alternatives: [SmolLM2-1.7B-Instruct](https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct) for text and [SmolVLM2-2.2B-Instruct](https://huggingface.co/HuggingFaceTB/SmolVLM2-2.2B-Instruct) for smaller multimodal inference. Choose by competence, observability, and resources—not filler uplift. Fix precision/quantization across conditions.

Training is not necessary for the inference-only scientific question. Current course acceptance must be confirmed with the TA/rubric. The instructor's [historical Fall 2021 handout](https://www.cs.columbia.edu/~zemel/Class/Nndl/project_handout.pdf) allows analysis projects but is not the current rubric. If training is required, substitute a bounded matched-training study for extension work and amend the specification before execution.

## Planned visual and navigation extensions

Render the same graphs with fixed node positions across edits, readable arrows, and redundant relation encodings. Keep the intervention unchanged across modalities. Report absolute modality effects and their difference; a nonsignificant interaction does not establish equivalence. One-hop/edge-extraction controls only imperfectly distinguish perception failures; perception-correct subset analyses are secondary.

Navigation tests H5 in a deterministic fully observable gridworld with position, orientation, walls, key, door, and goal. Begin with symbolic observations; add images only after vision feasibility. Compare C0, fixed C2, explicit intermediates, and an exact planner on paired worlds. Test route-relevant and irrelevant edits, balancing optimal path length across subgoal depths. Score membership in the set of optimal actions, episode success, collisions, action regret, successful-path efficiency, and total latency. Bootstrap world families and allow trajectories to diverge. Conclusions concern simulation, not physical robots or learned dynamics.

## Related work

See the [README literature list](../README.md#selected-literature). Additional counterfactual precedent: [DeFacto](https://arxiv.org/abs/2509.20912). Sources motivate controls and limit novelty claims; none constitutes JEVLab experimental evidence.
