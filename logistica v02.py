import PyPDF2
pdfFileObj = open('Lista 01 Expeditii-in-Borderou-1225134.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# print(pdfReader.numPages)
pageObj = pdfReader.getPage(1)
text = pageObj.extractText()
totalNumberOfPages = text.split()
primulNumar = totalNumberOfPages[1]
print (primulNumar)
alDoileaNumar = totalNumberOfPages[3]
print(alDoileaNumar)