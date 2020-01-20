#pdf merger
import PyPDF2
import os
import sys

#pdf_file_inputs = argv[1:]

current_folder = os.getcwd()
pdfnames = ['TEST1','TEST2','TEST3']
list_pdf = []

#input pages to be watermarked
for x in pdfnames:
    pdf_file = os.path.dirname(current_folder) + '/' + x
    list_pdf.append(pdf_file)
print(list_pdf)

#watermark pdf file
watermarktxt = os.path.dirname(current_folder) + '/' + 'wtr.pdf'
watermark = PyPDF2.PdfFileReader(open(watermarktxt, 'rb'))

# output 
output = PyPDF2.PdfFileWriter()

#def watermark(a,b):

for pdffiles in list_pdf:
    pdf_reader = PyPDF2.PdfFileReader(open(pdffiles + '.pdf', 'rb'))
    pages = pdf_reader.getNumPages()
    for i in range(pages):
        page = pdf_reader.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)
        #storing the watermarked files in the same folder
        with open (pdffiles + '_watermarked' + '.pdf', 'wb') as new_file:
            output.write(new_file)
