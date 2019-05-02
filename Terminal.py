import string
import sys
from Entry import Field
from Entry import Entry
from Table import Table
from Database import Database
from System import System

def main():
    system = System()
    while True:
        # Read input
        data = input("-> ")

        # Split input at space
        array = data.split()

        # First element in array is the op
        op = array[0]
        
        # Make operation lowercase
        op = op.lower()

        # Remove first element from the array
        array = array[1:len(array)]

        if (op == "db"):
            database = Database(array[0])
            system.addDatabase(database)
        elif (op == "tb"):
            # First entry is database.tablename
            database_name, table_name = array[0].split(".")
            database_name, table_name = database_name.lower(), table_name.lower()

            # Columns make up the rest of the entries
            columns = []
            for entry in array[1:]:
                column = entry
                columns.append(column)

            table = Table(table_name, columns)

            # Find database by name
            database: Database = None
            for db in system.databases:
                if (db.name == database_name):
                    database = db
                    break

            # Add table to database
            if (database is None):
                print("Database with name \'{database}\' could not be located".format(database=database_name))
            else:
                database.addTable(table)
        elif (op == "add"):
            # First entry is datbase.tablename
            database_name, table_name = array[0].split(".")
            database_name, table_name = database_name.lower(), table_name.lower()

            # Find database by name
            database: Database = None
            for db in system.databases:
                if (db.name == database_name):
                    database = db
                    break

            # Add table to database
            if (database is None):
                print("Database with name \'{database}\' could not be located".format(database=database_name))
            else:
                # Find table
                table: Table = None
                for tb in database.tables:
                    if (tb.name == table_name):
                        table = tb
                        break

                if (table is None):
                    print("Table with name \'{table}\' could not be located on database \'{database}\'".format(table=table_name, database=database_name))
                else:
                    # The rest of the parameters are fields
                    fields = []
                    for item in array[1:]:
                        name, value = item.split(":")
                        field = Field(name, value)
                        fields.append(field)

                    entry = Entry(fields)
                    table.addEntry(entry)
        elif (op == "sel"):
            database_name, table_name = array[0].split(".")

            # Find database by name
            database: Database = None
            for db in system.databases:
                if (db.name == database_name):
                    database = db
                    break

            # Find table
            table: Table = None
            for tb in database.tables:
                if (tb.name == table_name):
                    table = tb
                    break

            if (table is None):
                print("Table with name \'{table}\' could not be located on database \'{database}\'").format(table=table_name, database=database_name)
            else:
                table.print()
        elif (op == "exit"):
            info = system.getInfo()
            print("Removed {databases} database(s), {tables} table(s), {Entrys} Entry(s)".format(databases = info[0], tables = info[1], Entrys = info[2]))
            sys.exit(0)

    
    

main()