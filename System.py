from Database import Database

class System:
    def __init__(self):
        self.databases: list[Database] = []
    def addDatabase(self, database: Database) -> bool:
        for db in self.databases:
            if (db.name == database.name.lower()):
                print('Failed to add database \'{database}\'... Duplicate already exists with same name'.format(database=database.name))
                return False
        self.databases.append(database)

        print('Successfully added database \'{database}\' to the System'.format(database=database.name))
        return True
    def getInfo(self) -> (int, int, int):
        databases: int = 0
        tables: int = 0
        Entrys: int = 0
        for database in self.databases:
            for table in database.tables:
                for Entry in table.Entrys:
                    Entrys += 1
                tables += 1
            databases += 1
        
        return (databases, tables, Entrys)