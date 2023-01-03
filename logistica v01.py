import PyPDF2
import re

pdfFileObj = open('A6.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# print(pdfReader.numPages)
pageObj = pdfReader.getPage(0)
text = pageObj.extractText()

def is_phrase_in(phrase, textPagina):
    return re.search(r"\b{}\b".format(phrase), textPagina, re.IGNORECASE) is not None

phrase = "2 din"

if is_phrase_in(phrase, text) is True:
    print(text)
else:
    print("nu exista asa ceva")