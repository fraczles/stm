from subprocess import Popen, PIPE
from docx import opendocx, getdocumenttext
from os import walk
import unicodedata


#http://stackoverflow.com/questions/5725278/python-help-using-pdfminer-as-a-library
from openpyxl import load_workbook
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    count = 0
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        count += 1 
        print("Processing page: " + str(count))
        interpreter.process_page(page)
    fp.close()
    device.close()
    string = retstr.getvalue()
    retstr.close()
    return string


def sheet_to_text(file_path):
    wb = load_workbook(file_path)
    sheet_name = wb.get_sheet_names()[0]
    sheet = wb[sheet_name] 
    string = ""
    table = [row for row in sheet.rows]
    count = 0
    for row in sheet.rows:
        count += 1
    for i in range(count):
        if table[i][-1].value is not None:
            string += table[i][-1].value.encode('ascii', 'ignore')
    return string

def document_to_text(filename, file_path):
    if filename[-4:].lower() == ".doc":
        cmd = ['antiword', file_path]
        p = Popen(cmd, stdout=PIPE, shell=True)
        stdout, stderr = p.communicate()
        return stdout.decode('ascii', 'ignore')
    elif filename[-5:].lower() == ".docx":
        document = opendocx(file_path)
        paratextlist = getdocumenttext(document)
        newparatextlist = []
        for paratext in paratextlist:
            newparatextlist.append(paratext.encode("utf-8"))
        return '\n\n'.join(newparatextlist)
    elif filename[-4:].lower() == ".odt":
        cmd = ['odt2txt', file_path]
        p = Popen(cmd, stdout=PIPE)
        stdout, stderr = p.communicate()
        return stdout.decode('ascii', 'ignore')
    elif filename[-4:].lower() == ".pdf":
        return convert_pdf_to_txt(file_path)

pdfpath = "./pdfs"
for (dirpath, dirnames, filenames) in walk(pdfpath):
    for f in filenames:
        file_path = dirpath + "/" + f
        print("Converting " + f + " to plain text...")
        f_out = open(pdfpath+"/"+f[:-4]+'.txt', 'w')
        f_out.write(str(document_to_text(f, file_path)))
        f_out.close()

sheetpath = "./xlsx"
for (dirpath, dirnames, filenames) in walk(sheetpath):
    for f in filenames:
        if f[-5:] == ".xlsx":
            file_path = dirpath + "/" + f
            print("WRITING OUT TO:" + f)
            f_out = open(sheetpath+"/"+f[:-5]+'.txt', 'w')
            f_out.write(str(sheet_to_text(file_path)))
            f_out.close()

