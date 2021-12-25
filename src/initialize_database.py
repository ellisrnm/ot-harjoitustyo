import os
from database_connection import get_db_connection

def initialize_db():
    connection = get_db_connection()
    cursor = connection.cursor()
    dirname = os.path.dirname(__file__)
    schema_file_path = os.path.join(dirname, "schema.sql")
    cursor.executescript(open(schema_file_path, "r", encoding="utf-8").read())
    connection.commit()
    schema_file_path.close()

if __name__ == "__main__":
    initialize_db()
