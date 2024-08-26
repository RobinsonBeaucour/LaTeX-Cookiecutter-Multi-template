import os
import shutil

# Get the selected documentclass option from cookiecutter context
documentclass_option = "{{ cookiecutter.documentclass }}"

# Define the files and directories to delete based on the selected option
TO_DELETE = {
    "article": ["beamer.tex", "book.tex", "elsarticle.tex", "01_Chapters", "01_Sections_beamer"],
    "beamer": ["article.tex", "book.tex", "elsarticle.tex", "01_Chapters", "01_Sections"],
    "book": ["article.tex", "beamer.tex", "elsarticle.tex", "01_Sections_beamer", "01_Sections"],
    "elsarticle": ["article.tex", "beamer.tex", "book.tex", "01_Sections_beamer", "01_Chapters"],
}

# Determine the key based on the documentclass option
if documentclass_option == "book (for thesis or large report)":
    key_template = "book"
    os.rename('book.tex', 'main.tex')
elif documentclass_option == "article (for scientific paper or small report)":
    key_template = "article"
    os.rename('article.tex', 'main.tex')
elif documentclass_option == "elsarticle (for elsevier publication)":
    key_template = "elsarticle"
    os.rename('elsarticle.tex', 'main.tex')
elif documentclass_option == "beamer (for presentation)":
    key_template = "beamer"
    os.rename('beamer.tex', 'main.tex')
else:
    key_template = None

# Delete the corresponding files and directories
if key_template and key_template in TO_DELETE:
    for path in TO_DELETE[key_template]:
        path = path.strip()  # Ensure the path has no leading/trailing spaces
        if path and os.path.exists(path):
            if os.path.isfile(path):
                os.remove(path)
            elif os.path.isdir(path):
                shutil.rmtree(path)  # Use shutil.rmtree to remove non-empty directories

workflow = "{{ cookiecutter.workflow }}"

if workflow != "gitlab":
    os.remove(".gitlab-ci.yml")
if workflow != "github":
    shutil.rmtree(".github")
