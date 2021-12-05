import os
import sqlite3

db_file_path = os.path.join("..","data","database.sqlite")
connection = sqlite3.connect(db_file_path)
connection.row_factory = sqlite3.Row

def get_db_connection():
    return connection