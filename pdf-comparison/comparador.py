#import the PyPDF2 module
import PyPDF2

#open the PDF file
PDFfile = open('sample.pdf.', 'rb')

PDFfilereader = PyPDF2.PdfFileReader(PDFfile)

#print the number of pages
print(PDFfilereader.numPages)

#provide the page number
pages = PDFfilereader.getPage(85)

#extracting the text in PDF file
print(pages.extractText())

#close the PDF file
PDFfile.close()
