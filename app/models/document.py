class Document:
    def __init__(self, name,content):
        self.name = name
        self.content = content
    
    def get_name(self):
        return self.name

    def get_content(self):
        return self.content