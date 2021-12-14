from database_connection import get_db_connection
from entities.subproject import SubProject

def subproject_by_row(row):
    if not row:
        return None 
    return SubProject(row["id"], row["name"], row["description"], row["project_id"])

class SubProjectRepository:#
    def __init__(self, connection):
        self._connection = connection

    def create(self, name, project_id, description=""):
        cursor = self._connection.cursor()
        sql = "INSERT INTO SubProjects (name, description, project_id) VALUES (?, ?, ?);"
        cursor.execute(sql, (name, description, project_id))
        self._connection.commit()

    def fetch_all_from_project(self, project_id):
        cursor = self._connection.cursor()
        sql = "SELECT id, name, description, project_id FROM SubProjects WHERE project_id=?;"
        cursor.execute(sql, (str(project_id),))
        rows = cursor.fetchall()
        return list(map(subproject_by_row, rows))

    def get_subproject_id(self, project_id, subproject_name):
        cursor = self._connection.cursor()
        sql = "SELECT id FROM SubProjects WHERE project_id=? AND name=?;"
        cursor.execute(sql, (project_id, subproject_name))
        subproject_id = cursor.fetchone()[0]
        return subproject_id

subproject_repository = SubProjectRepository(get_db_connection())