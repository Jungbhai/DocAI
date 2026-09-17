from models.document import Document

class TXTDocument(Document):

    def extract_text(self):
        return "This is text extracted from a TXT"