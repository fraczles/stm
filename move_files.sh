if [ ! -d ./pdfs ]; then
  mkdir -p ./pdfs
fi

if [ ! -d ./docs ]; then
  mkdir -p ./docs
fi

if [ ! -d ./xlsx ]; then
  mkdir -p ./xlsx
fi


if [ ! -d ./raw_corpus ]; then
  mv Initial\ Text\ Corpus/ raw_corpus/
fi

find ./raw_corpus -name "*.pdf" -print0 | xargs -0 -I {} cp {} ./pdfs/
find ./raw_corpus -name "*.doc" -print0 | xargs -0 -I {} cp {} ./docs/
find ./raw_corpus -name "*.DOC" -print0 | xargs -0 -I {} cp {} ./docs/
find ./raw_corpus -name "*.xlsx" -print0 | xargs -0 -I {} cp {} ./xlsx/
