from database_connection import get_db_connection
from entities.subproject import SubProject

def subproject_by_row(row):
    if not row:
        return None 
    return SubProject(row["id"], row["name"], row["description"], row["project_id"])

class SubProjectRepository:#
    def __init__(self, connection):
        self._connection = connection

    def create(self, name, description=""):
        cursor = self._connection.cursor()
        sql = "INSERT INTO SubProjects (name, description) VALUES (?, ?)"
        cursor.execute(sql, (name, description))
        self._connection.commit()

    def fetch_all_from_project(self, project_id):
        cursor = self._connection.cursor()
        sql = "SELECT id, name, description, project_id FROM SubProjects WHERE project_id=?"
        cursor.execute(sql, (project_id,))
        rows = cursor.fetchall()
        return list(map(subproject_by_row, rows))

subproject_repository = SubProjectRepository(get_db_connection())