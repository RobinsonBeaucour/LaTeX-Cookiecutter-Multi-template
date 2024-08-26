# Scripts

## build.pl

This script must be used with MikTex, this script activate `pdflatex` and `bibtex` to generate PDF with SyncTeX file.

Example of use:

```bash
perl 00_Scripts/build.pl --file=main.tex
```

## latexdiff.pl

Latexdiff is a Perl script for visual mark up and revision of significant differences between two LaTeX files. See (LaTeXdiff)[https://www.ctan.org/pkg/latexdiff]

Example of use:

```bash
perl 00_Scripts/latexdiff.pl old.tex new.tex > diff.tex
```
> ⚠️ **If you are using Microsoft Powershell**: The output might not be UTF-8 encoded <br>
> Use `$PSDefaultParameterValues['Out-File:Encoding'] = 'utf8'` if the output file is wrongly encoded.

## latexpand.pl

Latexpand is a Perl script that simply replaces \input and \include commands with the content of the input or included file. See (LaTeXpand)[https://ctan.org/pkg/latexpand?lang=en]

Example of use:

```bash
perl 00_Scripts/latexpand.pl main.tex > concatenate.tex
```
> ⚠️ **If you are using Microsoft Powershell**: The output might not be UTF-8 encoded <br>
> Use `$PSDefaultParameterValues['Out-File:Encoding'] = 'utf8'` if the output file is wrongly encoded.

## latexrevise.pl

See (LaTeXdiff)[https://www.ctan.org/pkg/latexdiff] documentation.

## texcount.pl

TeXcount is a Perl script for counting words in LaTeX documents. It parses valid LaTeX documents counting words, headers, formulae (mathematics) and floats/begin-end groups. See (TeXcount)[https://app.uio.no/ifi/texcount/]

Example of use:

```bash
> perl 00_Scripts/texcount.pl concatenate.tex

File: concatenate.tex
Encoding: ascii
Words in text: 2439
Words in headers: 34
Words outside text (captions, etc.): 17
Number of headers: 14
Number of floats/tables/figures: 2
Number of math inlines: 16
Number of math displayed: 14
Subcounts:
  text+headers+captions (#headers/#floats/#inlines/#displayed)
  226+14+0 (2/0/0/0) _top_
  2+1+0 (1/0/0/0) Section: Introduction
  585+1+0 (1/0/0/0) Subsection: Context
  1047+1+0 (1/0/0/0) Subsection: State-of-the-art
  0+4+0 (1/0/0/0) Section: System investigated and methods
  170+2+4 (1/1/5/0) Subsection: Modeling approach} \label{Models
  16+2+0 (1/0/0/0) Section: MILP models} \label{app:model
  27+2+0 (1/0/0/0) Subsection: Renewable production} \label{Renewable_production
  83+2+0 (1/0/8/3) Subsection: Grid Flow} \label{Grid_Flow} \label{eq:F
  27+1+0 (1/0/0/2) Subsection: Converters} \label{Converter} \label{eq:C
  24+1+0 (1/0/2/2) Subsection: Compressors} \label{Compressor} \label{eq:K
  47+1+0 (1/0/1/6) Subsection: Storage} \label{Storage} \label{eq:S
  185+2+13 (1/1/0/1) Section: MILP tolerance} \label{app:MILP
```