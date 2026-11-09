# ReasonSpace course proposal

Two-page COMS W4776 proposal, including references. Prepared 2026-11-09 from `../research_proposal.md` and `../roadmap.md` at repository commit `00d9141`.

## Files

- `reasonspace_proposal.pdf`: compiled, visually inspected submission document.
- `reasonspace_proposal.tex`: editable LaTeX source.
- `references.bib`: seven primary-source citations, with linked arXiv identifiers.
- `neurips_2026.sty`: exact style text supplied by the user in the conversation; unchanged. Its declared package name determines the filename.

The original course URL returned HTTP 401. The subsequently pasted course style was used instead of the public conference-template fallback. The source uses the style's `preprint` option to show author names. Only its notice text is overridden to identify a Columbia course proposal rather than claim a conference submission. No margins, fonts, or section spacing are overridden.

## Rebuild

From this directory, with an existing TeX Live installation:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build reasonspace_proposal.tex
```

The checked build used TeX Live 2026, pdfLaTeX, BibTeX, and latexmk. Build products were kept outside the repository during preparation. The delivered PDF has two US Letter pages, resolved citations, and no overfull/underfull box or LaTeX warnings. Both final pages were rendered and inspected.

Bibliographic author lists and titles were checked against the primary arXiv records. Years identify the initial preprints (e.g., Mull-Tokens 2025), not later conference appearances. The proposal cites results as prior work and makes no preliminary-result claims.

## Assumptions to confirm

- Available GPU allocation and runtime: estimates are provisional, pending profiling.
- Whether the current course rubric requires training: the planned core is inference-only.
- Vision remains gated by perception quality and resources; navigation is future work.

No experiments, dependency installations, or model downloads were performed to prepare this proposal.
