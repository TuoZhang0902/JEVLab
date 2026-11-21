# ReasonSpace research specification

**Question.** When a model predicts where an agent ends up after four moves, does future-state supervision make it use the position recorded in its second latent slot? We will compare two training objectives on four-move routes with exactly four learned slots. This is a proposed experiment for COMS W4776. [Course proposal](proposal/reasonspace_proposal.pdf) · [Implementation roadmap](roadmap.md)

## Benchmark and splits

An agent moves on a deterministic 6 × 6 RGB grid. Coordinates start at (1, 1) in the top left. Moves into walls or across the boundary leave the agent in place. The four supplied moves determine the final cell. Use static walls and position as the full dynamic state so the simulator can resume from any legal halfway cell.

Generate an original map, a relevant edit that relocates a wall and changes the final cell, and an irrelevant edit that relocates an off-path wall and preserves the entire route. Save each map, the moves, the four visited cells, and the final answer. Present the same four distinct candidate cells in the same order for all three variants. Balance correct answer letters across families. Keep all variants and any symbolic views together in train, development, or test. Reject duplicate map/query combinations across splits.

The confirmation set contains 400–600 held-out **four-step families**. Choose the exact count using the pilot before opening the test set. One-step families belong to the perception pilot. A text rendering of the same grid can help diagnose failures to read the image.

## One slot per move

Use the same revision of Qwen2.5-VL-3B-Instruct in both runs. The decoder receives the initial image and a fixed instruction, then move 1, slot 1, move 2, slot 2, move 3, slot 3, move 4, slot 4, followed by the candidate cells and the answer cue. Each slot is a learned input embedding. Its contextual state can depend on the initial scene and moves supplied so far. This ordering keeps later moves and answer choices outside the second slot's causal context. The training target is the letter for the final cell.

| Condition | Objective |
| --- | --- |
| L1, answer-only LoRA | Final-answer cross-entropy. |
| L2, future-state-supervised LoRA | The same answer loss plus a weighted average of four frame-alignment losses. Slot 1 targets the frame after move 1, through slot 4 and the frame after move 4. |

For L2, minimize one minus the cosine similarity between a linear projection of each slot state and the corresponding frame embedding. Use the residual stream after the middle decoder block (block ⌊D/2⌋, one-based, for D blocks) for supervision, probes, and swaps. Mean-pool the frozen vision encoder's spatial features of each simulator frame to obtain a fixed-width target. Verify in the pilot that the targets distinguish neighboring agent positions on the same map. The projection head is used only for the auxiliary loss. Only the initial image is supplied to the decoder.

Match checkpoint revision, initial slot embeddings and adapters, LoRA rank and target modules, examples, order, optimizer, number of updates, precision, and decoding. Freeze the alignment weight and training budget on development data. Record one shared training seed. With one matched pair, test-family intervals describe these two fitted models. Variation across training seeds remains an open question.

## Outcomes and interpretation

1. **Primary behavioral outcome.** Score a family as one only when both the original and relevant-edit answers are correct. Use answer-letter logits at the answer cue and audit greedy outputs on a subset. Report each model's score and the paired L2 minus L1 difference. Use a 95% bootstrap interval with 10,000 draws of whole test families. The practical benefit threshold is +5 percentage points. Report whether the interval lies above, below, or crosses that threshold. Also report individual-map accuracy and joint correctness on the original and irrelevant edit.
2. **Primary mechanism test.** Measure whether replacing the second slot shifts the answer toward the endpoint implied by its donor position. Apply the prespecified swap and control below to both models on identical eligible families.
3. **Supporting probes.** Fit a linear coordinate classifier on each frozen slot using training families. Select regularization on development families and report held-out accuracy for the position after the corresponding move. Compare with a majority-cell baseline and the same probe on the preceding move token. These probes measure what can be read from each representation.

### Directional step-two swap

- Use the original map as recipient A, its relevant edit as donor B, and its irrelevant edit as control C. All three receive the same four moves. Require B to reach a different position after move two and C to reach the same position as A. The donor position must be traversable on A's map.
- Before model inference, start the simulator at B's step-two cell **on A's map**, execute A's last two moves, and save the predicted alternative cell. Require it to differ from A's clean ground-truth endpoint and to appear among A's choices. Freeze eligibility from simulator facts alone and report the eligible count and fraction. Keep all families in the behavioral analysis.
- For each model, replace only A's slot-two residual vector at the specified block with the corresponding vector from B. Repeat from a clean A run with C as the donor. Recompute downstream activations and answer probabilities with A's input. A self-swap must reproduce the clean logits within the recorded numerical tolerance.
- For each patch, subtract A's clean probability of the predicted alternative from its patched probability of **that same alternative**, normalized over the four choices. The family score is the different-position shift minus the same-position shift. Report both shifts, the family score for each model, and the paired L2 minus L1 difference with a 95% interval from 10,000 resamples of eligible families.
- A positive shift toward the predicted cell beyond the control supports use of step-two state information at the tested site. A larger contrast for L2 supports the supervision hypothesis. Report the clean behavioral score alongside this result. An accuracy gain alone leaves the mechanism unresolved, and a small patch effect can also reflect information carried at other positions or layers.

## Scope and related work

The core deliverable is the matched L1/L2 pair, behavioral results, and directional swap. Inference-only no-filler, dot-placement, or explicit-reasoning comparisons are secondary extensions if resources permit. The 25–45 GPU-hour allowance on a single 24 GB GPU is provisional.

Ablate-to-Validate found that replacing token content often preserved much of the accuracy gain. WM-VLM found a sharp performance drop when its generated intermediate visual states were removed or corrupted on mental rotation tasks. The grid experiment holds the model and task fixed and tests the destination predicted by a specific state substitution. [Ablate-to-Validate](https://arxiv.org/abs/2605.21642) · [WM-VLM](https://arxiv.org/abs/2609.34826)
