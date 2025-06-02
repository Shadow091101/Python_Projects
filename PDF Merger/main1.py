import PyPDF2
import os

pdfMerger=PyPDF2.PdfMerger()

all_pdf_file_name=[i for i in os.listdir() if i.endswith('.pdf')]

print(all_pdf_file_name)

for filename in all_pdf_file_name:
    all_pdf_file_name=open(filename,'rb')
    pdfReader=PyPDF2.PdfReader(all_pdf_file_name)
    pdfMerger.append(pdfReader)
all_pdf_file_name.close()
pdfMerger.write('merged.pdf')

