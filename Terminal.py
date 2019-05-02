import string
import sys
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

            # Columns make up the rest of the entries
            columns = []
            for Entry in array[1:]:
                column = Entry
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
        elif (op == "exit"):
            info = system.getInfo()
            print("Removed {databases} database(s), {tables} table(s), {Entrys} Entry(s)".format(databases = info[0], tables = info[1], Entrys = info[2]))
            sys.exit(0)

    
    

main()