# pdf reader
import PyPDF2
import os
import unicodedata
import re

#os.path.dirname
#os.path.abspath
current_folder = os.getcwd()
print(f'dirname : {os.path.dirname(current_folder)}')

#print(f'dirname : {os.path.abspath(current_folder)}')
#print(f'basename : {os.path.basename(current_folder)}')
pdf_file = os.path.dirname(current_folder) + '/' + 'TEST1.pdf'
with open( pdf_file, 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    page = reader.getPage(0)
    page_content = page.extractText()
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    print(f"the text is : {(page)}")
    with open ('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)
    
   
    