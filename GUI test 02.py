import PyPDF2
from copy import copy

from tkinter import *
from tkinter import filedialog
myWindow = Tk()
myWindow.title("Borderouri Dragon Star")
myWindow.geometry("300x300")

def inputFile (userInput):
    pdf1File = open(userInput, 'rb')
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

    pdfOutputFile1 = open(userInput+' - borderou A4.pdf', 'wb')
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

    pdfOutputFinal = open(userInput + " - borderou A6.pdf", "wb")
    pdfWriterFinal.write(pdfOutputFinal)
    pdfOutputFinal.close()
    return


def browseFunc():
    filename = filedialog.askopenfilename(filetypes = (("Adobe Acrobat'", "*.pdf"), ("All files", "*.*")))
    pathLabel.config(text=filename)
    inputFile(filename)
    return

selectLabel = Label(myWindow)
selectLabel.config(text="Please select the PDF file")
selectLabel.pack()

browsebutton = Button(myWindow, padx=20, pady=0 ,text="Browse", command= browseFunc)
browsebutton.pack(side=TOP)

pathLabel = Label(myWindow)
pathLabel.pack()

myWindow.mainloop()