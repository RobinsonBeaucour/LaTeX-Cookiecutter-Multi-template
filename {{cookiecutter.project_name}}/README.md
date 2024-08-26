# {{ cookiecutter.project_name }}

Author:
* {{ cookiecutter.author_name}} <{{ cookiecutter.author_email}}>, {{ cookiecutter.institute }}

## Abstract

### {{ cookiecutter.title }}

{{ cookiecutter.abstract }}

## Recommanded setup

* Local IDE : [VS code](https://code.visualstudio.com/)

    With extensions
    * [LateX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop)

* Perl

    For Windows
    * [StrawberryPerl](https://strawberryperl.com/)

* TeX Distribution

    For Windows
    * [MikTex](https://miktex.org/)

## Perl Scripts

`00_Scripts` folder contains perl script usefull to process TeX file. See [Script documentation](./00_Scripts/README.md) for more informations.

{% if cookiecutter.workflow == "github" %}
## GitHub Workflow

### build.yaml

This workflow is triggered on any changes in `main` branch.

The first job generate a concatenated TeX file and a word count.

The second job generate PDF from the concatenated TeX file.

The workflow can be manually triggered

### diff.yaml

This workflow is triggered on any changes in a branch that is in a pull request for `main` branch.

The first job generate a concatenated TeX file, a word count and a diff TeX file with `main.tex` from `main` branch.

The second job generate PDF from the concatenated new TeX file and the diff Tex file.

The workflow can be manually triggered

{% elif cookiecutter.workflow == "gitlab" %}
## GitLab Workflow

### process & build

This workflow is triggered on any changes in `main` branch.

The first job generate a concatenated TeX file and a word count.

The second job generate PDF from the concatenated TeX file.

The workflow can be manually triggered

### diff_process & diff_build

This workflow is triggered on any changes in a branch that is in a pull request for `main` branch.

The first job generate a concatenated TeX file, a word count and a diff TeX file with `main.tex` from `main` branch.

The second job generate PDF from the concatenated new TeX file and the diff Tex file.

The workflow can be manually triggered

{% endif %}

