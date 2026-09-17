from models.document import Document

class PDFDocument(Document):

    def extract_text(self):
        return "This is text extracted from a PDF"