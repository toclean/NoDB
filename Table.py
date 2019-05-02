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
    def removeEntry(self, id) -> bool:
        toRemove = []
        for i in range(0, len(self.entries)):
            entry = self.entries[i]
            identifier = str(entry.identifier).lower()
            if (identifier.startswith(id.lower()) or identifier.lower() == id.lower()):
                toRemove.append(i)
                # self.entries.pop(i)
                # print("Successfully removed entry from table \'{table}\'".format(table=self.name))
                # return True
        if (len(toRemove) == 1):
            entry = self.entries.pop(toRemove[0])
            print("Successfully removed entry {entry} from table \'{table}\'".format(entry=entry.identifier, table=self.name))
            return True
        else:
            print("Failed to remove entry from table \'{table}\' there were multiple entries with that id".format(table=self.name))
            return False
    def print(self) -> None:
        for entry in self.entries:
            output = str(entry.identifier) + " "
            for field in entry.fields:
                output += "(" + field.name + "|" + field.value + ")\t"
            print(output)
    
class Column:
    def __init__(self, name: str):
        self.name: str = name
        self.used: bool = False