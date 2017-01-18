if [ ! -d ./corpus ]; then
  mkdir -p ./corpus
fi

find ./ -name "*.txt" -print0 | xargs -0 -I {} mv {} ./corpus/
