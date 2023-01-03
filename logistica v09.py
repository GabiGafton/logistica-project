import PyPDF2
from copy import copy
import re

from tkinter import *
from tkinter import filedialog as fd

a = Tk()

def mFileOpen():
    #file1 = filedialog.askopenfilename(filetypes = (("Acrobat File", "*.pdf"), ("All Files", "*.*")))
    #label = Label(text=file1).pack()
    #output = file1
    filename = fd.askopenfilename()
    print(filename)

button = Button(text="Open File", width = 30, command = mFileOpen).pack()

a.mainloop()

pdf1File = open(mFileOpen(), 'rb')
pdfReader = PyPDF2.PdfFileReader(pdf1File)
pdfWriter1 = PyPDF2.PdfFileWriter()
pdfWriter2 = PyPDF2.PdfFileWriter()

for pageNum in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    text = pageObj.extractText()
    totalNumberOfPages = text.split()
    primulNumar = totalNumberOfPages[1]
    if primulNumar == "1":
        pageObj1 = pdfReader.getPage(pageNum)
        pdfWriter1.addPage(pageObj1)
    else:
        pageObj2 = pdfReader.getPage(pageNum)
        pdfWriter2.addPage(pageObj2)

pdfOutputFile1 = open('A4.pdf', 'wb')
pdfWriter1.write(pdfOutputFile1)
pdfOutputFile1.close()

pdf1File.close()

pdfOutputFile2 = open('temp000.pdf', 'wb')
pdfWriter2.write(pdfOutputFile2)
pdfOutputFile2.close()

final = open("temp000.pdf", "rb")
pdfReaderFinal = PyPDF2.PdfFileReader(final)
pdfWriterFinal = PyPDF2.PdfFileWriter()

for i in range(pdfReaderFinal.numPages):
    page = pdfReaderFinal.getPage(i)
    totTextulDinPagina = page.extractText()
    #print(totTextulDinPagina.count("Expeditor"))
    if totTextulDinPagina.count("Expeditor") == 4:
        x = copy(page)
        y = copy(page)
        v = copy(page)
        z = copy(page)
        x.cropBox.setUpperLeft((0,841.89))
        x.cropBox.setLowerLeft((0,420.945))
        x.cropBox.setUpperRight((297.638,841.89))
        x.cropBox.setLowerRight((297.638,420.945))
        pdfWriterFinal.addPage(x)

        y.cropBox.setUpperLeft((297.638,841.89))
        y.cropBox.setLowerLeft((297.638,420.945))
        y.cropBox.setUpperRight((595.276,841.89))
        y.cropBox.setLowerRight((595.276,420.945))
        pdfWriterFinal.addPage(y)

        v.cropBox.setUpperLeft((0,420.945))
        v.cropBox.setLowerLeft((0,0))
        v.cropBox.setUpperRight((297.638,420.945))
        v.cropBox.setLowerRight((297.638,0))
        pdfWriterFinal.addPage(v)

        z.cropBox.setUpperLeft((297.638,420.945))
        z.cropBox.setLowerLeft((297.638,0))
        z.cropBox.setUpperRight((595.276,420.945))
        z.cropBox.setLowerRight((595.276,0))
        pdfWriterFinal.addPage(z)

    elif totTextulDinPagina.count("Expeditor") == 3:
        x = copy(page)
        y = copy(page)
        v = copy(page)
        x.cropBox.setUpperLeft((0,841.89))
        x.cropBox.setLowerLeft((0,420.945))
        x.cropBox.setUpperRight((297.638,841.89))
        x.cropBox.setLowerRight((297.638,420.945))
        pdfWriterFinal.addPage(x)

        y.cropBox.setUpperLeft((297.638,841.89))
        y.cropBox.setLowerLeft((297.638,420.945))
        y.cropBox.setUpperRight((595.276,841.89))
        y.cropBox.setLowerRight((595.276,420.945))
        pdfWriterFinal.addPage(y)

        v.cropBox.setUpperLeft((0,420.945))
        v.cropBox.setLowerLeft((0,0))
        v.cropBox.setUpperRight((297.638,420.945))
        v.cropBox.setLowerRight((297.638,0))
        pdfWriterFinal.addPage(v)

    elif totTextulDinPagina.count("Expeditor") == 2:
        x = copy(page)
        y = copy(page)
        x.cropBox.setUpperLeft((0,841.89))
        x.cropBox.setLowerLeft((0,420.945))
        x.cropBox.setUpperRight((297.638,841.89))
        x.cropBox.setLowerRight((297.638,420.945))
        pdfWriterFinal.addPage(x)

        y.cropBox.setUpperLeft((297.638,841.89))
        y.cropBox.setLowerLeft((297.638,420.945))
        y.cropBox.setUpperRight((595.276,841.89))
        y.cropBox.setLowerRight((595.276,420.945))
        pdfWriterFinal.addPage(y)

    else:
        x = copy(page)
        x.cropBox.setUpperLeft((0,841.89))
        x.cropBox.setLowerLeft((0,420.945))
        x.cropBox.setUpperRight((297.638,841.89))
        x.cropBox.setLowerRight((297.638,420.945))
        pdfWriterFinal.addPage(x)


pdfOutputFinal = open("A6.pdf", "wb")
pdfWriterFinal.write(pdfOutputFinal)
pdfOutputFinal.close()

