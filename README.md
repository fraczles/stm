# General outline
The goal of these tools is to produce a `documents.csv` file -- a CSV summarizing the corpus. `documents.csv` contains two columns: `document_name`, `content` which pair a document name with its full text. The `stm` package in R requires this document to build models.

The tools listed in this directory facilitate the generation of `documents.csv`

# Workflow steps from scratch
NOTE: There may be dependencies you may need to install to run these scripts. I'll work on a solution to this soon.
1. Start in an empty directory
2. Run: `git pull https://github.com/fraczles/stm .`
3. Copy your corpus into the current directory, name it Initial Text Corpus (naming must be exact)
4. Run: `python driver.py`
   Note: `driver.py` is just a wrapper around the directories 4 main scripts: 
    1. `move_files.sh`
      -> renames corpus dir, aggregates all documents from corpus
    2. `to_plain.py`
      -> for all *.(pdf | doc | xlsx), generate equivalent *.txt
    3. `collect_txt.sh
      -> recursively move all .txt in directory to ./corpus/ 
    4. `tdm.py`
      -> generate `documents.csv` given all the *.txt in ./corpus


# Adding new documents to the corpus

Current approach is to:
1. Manually convert any new document to plaintext (new1.pdf -> new.txt, new2.pdf -> new2.pdf)
2. Add it to ./corpus/ `mv new.txt ./corpus/`
3. Generate a new documents matrix, `python tdm.py`

# Workflow in R
  1. Follow routines in `prep.R`, installing all required packages. Follow the documentation in the [stm vignette](https://cran.r-project.org/web/packages/stm/vignettes/stmVignette.pdf) starting around section 3.2 for instructions on how to pick a good model.
