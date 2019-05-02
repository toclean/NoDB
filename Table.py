from Entry import Entry

class Table:
    def __init__(self, name, columns):
        self.name = name
        self.columns = columns
        self.entries: List[Entry] = []
    def addEntry(self, entry) -> bool:
        if (entry is None):
            print('Failed to add entry as it was None')
            return False
        if (len(entry.fields) != len(self.columns)):
            print('Failed to add entry as the number of columns did not match')
            return False

        columns = []
        for col in self.columns:
            columns.append(Column(col))

        fields = []
        for field in entry.fields:
            for col in columns:
                if (col.name.lower() == field.name.lower()):
                    if (col.used == True):
                        print("Failed to add entry as their was a duplicate field \'{field}\'".format(field = field.name))
                        return False
                    col.used = True
                    fields.append(field)
                    break
        entry = Entry(fields)
        self.entries.append(entry)
        print("Successfully added entry to {table}".format(table=self.name))
    def print(self) -> None:
        for entry in self.entries:
            output = ""
            for field in entry.fields:
                output += "(" + field.name + "|" + field.value + ")\t"
            print(output)
    
class Column:
    def __init__(self, name: str):
        self.name: str = name
        self.used: bool = False