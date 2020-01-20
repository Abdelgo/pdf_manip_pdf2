#pdf merger
import PyPDF2
import os
import sys
import unicodedata
import re

#pdf_file_inputs = argv[1:]

current_folder = os.getcwd()
pdfnames = ['TEST1.pdf','TEST2.pdf','TEST3.pdf']
list_pdf = []

for x in pdfnames:
    pdf_file = os.path.dirname(current_folder) + '/' + x
    list_pdf.append(pdf_file)
print(list_pdf)

def pdf_merger(pdflist):
    pdfmerger = PyPDF2.PdfFileMerger()
    for pdf in pdflist:
        pdfmerger.append(pdf)
    pdfmerger.write(os.path.dirname(current_folder) + '/' + 'mergedpdf.pdf')


pdf_merger(list_pdf)
