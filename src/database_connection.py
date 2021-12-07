import os
import sqlite3

dirname = os.path.dirname(__file__)
db_file_path = os.path.join(dirname, "..","data","database.sqlite")
connection = sqlite3.connect(db_file_path)
connection.row_factory = sqlite3.Row

def get_db_connection():
    return connection