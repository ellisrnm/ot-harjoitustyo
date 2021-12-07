from database_connection import get_db_connection
from entities.project import Project

def project_by_row(row):
    if not row:
        return None 
    return Project(row["id"], row["name"])

class ProjectRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, name):
        cursor = self._connection.cursor()
        sql = "INSERT INTO Projects (name) VALUES (?)"
        cursor.execute(sql, (name,))
        self._connection.commit()

    def fetch_all(self):
        cursor = self._connection.cursor()
        sql = "SELECT id, name FROM Projects"
        cursor.execute(sql)
        rows = cursor.fetchall()
        return list(map(project_by_row, rows))

project_repository = ProjectRepository(get_db_connection())