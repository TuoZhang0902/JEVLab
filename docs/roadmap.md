# ReasonSpace implementation roadmap

The semester deliverable is one matched pair of four-step, four-slot LoRA runs. The central comparison asks whether supervision from each future frame changes the model's use of its halfway position. All milestones below are planned. [Research specification](research_proposal.md) · [Course proposal](proposal/reasonspace_proposal.pdf)

| Milestone | Work | Completion check |
| --- | --- | --- |
| 1. Benchmark | Generate original, relevant-edit, and irrelevant-edit 6 × 6 maps. Save simulator states after every move, shared answer choices, family IDs, and split manifests. | Replay all labels and hybrid endpoints. Verify family isolation, balanced answer letters, legal donor cells, and unchanged control routes. |
| 2. Pilot | Use 60 one-step families to check perception and 60 four-step families to estimate difficulty and swap eligibility. Profile a short L1 and L2 training run on the allocated GPU. | Target at least 85% one-step visual accuracy and 35–85% four-step baseline accuracy. If perception is limiting, inspect matched text views and try one renderer or resolution adjustment on development data. Record eligible counts, peak memory, and time per update. |
| 3. Training and intervention checks | Interleave each move with one learned slot. Extract the middle-block states and frozen frame targets. Implement answer scoring, slot-two swaps, and same-position controls. | Verify slot two cannot see moves three or four. Test frame sensitivity to a one-cell move. Confirm self-swaps reproduce clean logits and that each patch recomputes downstream activations. |
| 4. Protocol freeze and matched training | Fix the model revision, seed, family manifests, exact test count within 400–600, training-set size, optimizer, updates, LoRA settings, auxiliary loss weight, precision, and hook site. Train L1 and L2 on identical four-step examples in the same order. | Save both checkpoints and configurations. Verify matching slot/adapter initialization and training logs. Reserve intermediate frames for auxiliary targets. |
| 5. Held-out evaluation | Score both models on every four-step test family. Run both patches on all simulator-eligible families. Fit coordinate probes on training families and evaluate them on held-out families. | Report paired correctness with the +5-point practical threshold, irrelevant-edit joint correctness, clean and patched probabilities, control-adjusted directional shifts, eligible denominators, and paired family-bootstrap intervals. |
| 6. Course report | Regenerate figures and tables from saved per-family predictions and simulation records. | Discuss separately the behavioral effect, information decoded by probes, and effect of the directional intervention. Document null results, pilot changes, measured compute, and the single-seed limitation. |

## Team and compute

Confirm the GPU allocation, deadline, and division of work with the three-person team and TA mentor Todd Morrill. The benchmark owner produces the split and simulator records, the modeling owner trains both conditions, and the evaluation owner validates the swap and paired analysis.

| Work on one 24 GB GPU | Provisional allowance |
| --- | --- |
| Perception, training, and intervention pilots | 2–4 GPU-hours |
| Matched L1 and L2 training | 12–20 GPU-hours |
| Held-out predictions and coordinate probes | 5–10 GPU-hours |
| Directional swaps, controls, and reruns | 6–11 GPU-hours |
| **Total** | **25–45 GPU-hours** |

Replace these allowances with the pilot measurements before committing to a training schedule. If time is tight, drop optional inference-only filler comparisons first. Preserve the matched pair and both swap conditions. If resources only allow the pilot, report feasibility and leave the supervision question open.
