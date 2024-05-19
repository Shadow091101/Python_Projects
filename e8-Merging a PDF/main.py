from pypdf import PdfWriter

merger = PdfWriter()
files=['first.pdf','second.pdf','third.pdf','fourth.pdf','fifth.pdf','sixth.pdf','seventh.pdf']
for pdf in files:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()