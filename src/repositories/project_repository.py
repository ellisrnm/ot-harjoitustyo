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

    def get_project_id(self, project_name):
        cursor = self._connection.cursor()
        sql = "SELECT id FROM Projects WHERE name=?"
        cursor.execute(sql, (project_name,))
        project_id = cursor.fetchone()[0]
        return project_id

project_repository = ProjectRepository(get_db_connection())