from models.pdf_document import PDFDocument
from models.txt_document import TXTDocument

pdf = PDFDocument("report.pdf")
txt = TXTDocument("notes.txt")

print(pdf.name)
print(pdf.extract_text())

print(txt.name)
print(txt.extract_text())