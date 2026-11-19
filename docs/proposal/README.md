# ReasonSpace course proposal

Two-page English proposal for Columbia COMS W4776, updated November 19, 2026. The main study compares answer-only LoRA with future-state-supervised LoRA on four-move routes using one latent slot per move. The figure illustrates the original map and its two counterfactual variants.

## Source package

The archive contains the editable proposal, its TikZ figure inside the TeX file, the BibTeX database, the course style, and this README. Extract the ZIP and run the following command from the directory containing the TeX file. TeX Live with latexmk, pdfLaTeX, BibTeX, and TikZ is required.

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error reasonspace_proposal.tex
```

On macOS with both TinyTeX and MacTeX installed, select the full MacTeX toolchain with `export PATH="/Library/TeX/texbin:$PATH"` before running latexmk.

The output is `reasonspace_proposal.pdf`. The manuscript and bibliography contain all figure and citation inputs needed for the build.
