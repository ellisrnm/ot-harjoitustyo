from database_connection import get_db_connection

def initialize_db():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(open("schema.sql", "r").read())
    connection.commit()

if __name__ == "__main__":
    initialize_db()