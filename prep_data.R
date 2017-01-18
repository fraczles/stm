library(stm)
setwd("/Users/fraczak/Code/stimson/corpus")
data <- read.csv("documents.csv")
processed <- textProcessor(data$content)
out <- prepDocuments(processed$documents, processed$vocab)
docs <- out$documents
vocab <- out$vocab
selectors <- selectModel(docs, vocab, K = 5, max.em.its = 50, runs = 10)
