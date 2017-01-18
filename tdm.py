import textmining
import csv
import re


from os import listdir
from os.path import isfile, join



def termdocumentmatrix_example():
    # Create some very short sample documents
    tdm = textmining.TermDocumentMatrix()
    mypath = "./corpus"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    documents = open('documents.csv', 'w') 
    writer = csv.writer(documents)
    writer.writerow(('document_name', 'content'))
    pattern = r"(cid)+"
    for f in onlyfiles:
        if (f[-4:] == ".txt"):
            doc = open(mypath + "/" + f, 'r')
            txt = doc.read().replace(',', '')
            txt = ' '.join(txt.split())
            re.sub(pattern, "", txt) 
            
            writer.writerow((f, txt))
            tdm.add_doc(txt)
            doc.close
    documents.close() 
    
    # Initialize class to create term-document matrix
    # Add the documents
    #tdm.add_doc(doc1)
    #tdm.add_doc(doc2)
    #tdm.add_doc(doc3)
    # Write out the matrix to a csv file. Note that setting cutoff=1 means
    # that words which appear in 1 or more documents will be included in
    # the output (i.e. every word will appear in the output). The default
    # for cutoff is 2, since we usually aren't interested in words which
    # appear in a single document. For this example we want to see all
    # words however, hence cutoff=1.
    tdm.write_csv('matrix.csv', cutoff=2)
    # Instead of writing out the matrix you can also access its rows directly.
    # Let's print them to the screen.
termdocumentmatrix_example()
