class Document:
    def __init__(self, name):
        self.name = name
    
    def extract_text(self):
        raise NotImplementedError("Subclasses must implement extract text()")