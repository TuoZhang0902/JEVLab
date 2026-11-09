# Implementation roadmap and collaboration gates

**Planning only.** No milestone below claims implementation or experimental completion. [Specification](research_proposal.md) · [Overview](../README.md)

## Before coding

Confirm the current rubric (including training requirements), GPU/VRAM and hours, deadline, ownership, checkpoint, fixed C2–C0 contrast, five-point practical threshold, and sample-size rule. Recheck teammate changes. Document any scope change in the proposal.

## Milestones

| Milestone | Proposed files within existing folders | Acceptance checks |
| --- | --- | --- |
| M0: Protocol | Future `configs/text_pilot.json`, `configs/text_confirmatory.json` | Reject missing seeds/revisions and unknown conditions |
| M1: Dataset | Future `src/graphs.py`, `src/dataset.py`, focused `tests/` | Hand-checked traversal, determinism, valid edits, degree preservation, balanced labels, split isolation |
| M2: Measurement | Future `src/model.py`, `src/interventions.py` | Exact token counts/positions, no special fillers, stable answers, batch/single and cached/prefill agreement |
| M3: Pilot | Future `src/evaluate.py`; `experiments/token_evidence/` | Resume without duplicates; retain errors; measured runtime/memory; gates below |
| M4: Core | Future `src/analyze.py`; frozen manifest and predictions | Hand-computed metric fixtures, paired bootstrap, depth weights, missing-condition detection, regenerable figures |
| M5: Vision | Future `src/render.py`, `configs/vision_pilot.json` | Fixed layout, graph/render correspondence, legibility, resolution/token controls |
| M6: Report | Results/reproduction instructions in `docs/` and `experiments/` | Claims trace to saved outputs; failed pilots and limitations disclosed |

These filenames are proposed, not existing modules. Keep generation, evaluation, and analysis independently runnable. Tests and generation must not download models; model integration checks require explicit opt-in. Notebooks are exploratory, not the sole source of final metrics.

## Text pilot

Use 60 families per depth: 180 families and 540 instances. C0–C4 yield 2,700 scored evaluations; add cached/prefill checks on 30 inputs and C6 on 60 originals.

Pass only if all generator/edit/split/token/scoring checks pass, one-hop baseline accuracy is at least 85%, at least one deeper baseline lies between 35% and 85%, and projected confirmation cost fits the allocation. These bands are engineering gates, not findings.

Permit one documented development-only benchmark revision. Persistent floor/ceiling performance requires review, not indefinite searching for filler gains. Zero/negative filler uplift does not fail the pilot. Freeze prompts, scoring, model revisions, contrast, and sample size before confirmation.

## Vision gate

Start with 60 development families and inspect all renderings. Target ≥85% one-hop endpoint accuracy and ≥90% targeted edge-extraction accuracy, with deeper performance above chance and usable headroom. Check image-token cost/runtime. Permit one renderer/resolution revision; otherwise report the perception bottleneck and defer the full extension.

After passing, compare C0 and fixed C2 on new matched text/image families, with C6 on a subset. Do not retune filler identity/count on images. Fix layouts across edits and retain full-population results alongside labelled conditional diagnostics.

## Navigation gate

Proceed only after the text core is complete and reproducible evidence sensitivity or a specific failure mode motivates closed-loop evaluation. Require remaining compute and reporting time. Follow [H5's protocol](research_proposal.md#planned-visual-and-navigation-extensions). Physical hardware, large simulators, and VLA training are not routine extensions.

## Resource estimates

Planning allowances, not measured compatibility or results; replace with pilot measurements.

| Work | Scale | Allowance |
| --- | --- | --- |
| Text pilot | About 3,000 evaluations | 1–4 GPU-hours |
| Confirmation | 400 families/depth × 3 variants × 6 conditions = 21,600 evaluations | 3–18 GPU-hours at 0.5–3 seconds/evaluation |
| Text diagnostics/intermediates/reruns | Selected subsets | 5–15 GPU-hours |
| Vision pilot/selected confirmation | Roughly 5,000–10,000 evaluations | 5–25 GPU-hours |

Reserve approximately 20–40 GPU-hours for text and another 10–30 for vision. Doubling families doubles confirmation evaluations. Plan Qwen inference around one 16–24 GB GPU with small batches/bounded resolution; smaller candidates may need less memory. Training needs a separately profiled budget and approval.

For two contributors, a provisional four-week sequence is benchmark/measurement, pilot/protocol freeze, confirmation/analysis, then reporting/gated vision. Actual dates depend on the deadline and availability. Protect reporting time before adding extensions.

## Reproducibility and review

Record repository commit/configuration hash; model/tokenizer/processor revisions; package versions; hardware, precision and attention backend; generator version/seeds; family/split IDs and hashes; assembled token IDs and filler offsets; image/visual-token metadata; choice scores, predictions, answers/errors; warm-up policy, latency, and memory. Preserve all pilot revisions.

The existing `requirements.txt` is unpinned and unvalidated. Pin a tested environment only after implementation approval. Never commit credentials or large weights/data. Check ignore rules so compact manifests and predictions remain tracked or have a documented artifact location.

Use focused branches and PRs to `main`; no force pushes or unrelated refactors. State hypothesis, changed behavior, checks/commands, observed outputs, cost, and limitations in experiment PRs. Separate documentation and experiment code. Review the diff and status before committing; preserve the teammate's proposal and Git history.
