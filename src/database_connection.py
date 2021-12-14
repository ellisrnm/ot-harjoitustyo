import os
import sqlite3
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)
try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

db_file_name = str(os.getenv('DATABASE_FILENAME')) 
db_file_path = os.path.join(dirname, "..", "data", db_file_name)
connection = sqlite3.connect(db_file_path)
connection.row_factory = sqlite3.Row

def get_db_connection():
    return connection