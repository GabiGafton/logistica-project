import PyPDF2
pdf1File = open('test.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdf1File)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    text = pageObj.extractText()
    totalNumberOfPages = text.split()
    primulNumar = totalNumberOfPages[1]
    if primulNumar == "1":
        pdfWriter.addPage(pageObj)
#        print(primulNumar)

pdfOutputFile = open('altceva.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1File.close()