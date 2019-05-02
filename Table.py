from Entry import Entry

class Table:
    def __init__(self, name, columns):
        self.name = name
        self.columns = columns
        self.entries = []
    def getEntry(self, entryname):
        for entry in self.entries:
            if (entry.name == entryname):
                return entry
        return None
    
    