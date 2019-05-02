from Entry import Entry
from Table import Table

class Database:
    def __init__(self, name) -> None:
        self.name: str = name
        self.tables: list[Table] = []
    def addTable(self, table) -> bool:
        for tb in self.tables:
            if (tb.name== table.name.lower()):
                print("Failed to add table \'{table}\' to database \'{database}\'... Duplicate already exists with same name".format(table=table.name, database=self.name))
                return False

        self.tables.append(table)
        print("Successfully added table \'{table}\' to database \'{database}\'".format(table=table.name, database=self.name))
        return True
    def getTable(self, tablename) -> Table:
        for table in self.tables:
            if (table.name == tablename.lower()):
                return table
        return None