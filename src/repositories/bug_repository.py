from database_connection import get_db_connection
from entities.bug import Bug

def bug_by_row(row):
    if not row:
        return None
    return Bug(row["id"], row["name"], row["description"],
               row["priority"], row["status"], row["subproject_id"])

class BugRepository:
    def __init__(self, connection):
        self._connection = connection

    def fetch_all_from_subproject(self, subproject_id, status=None):
        cursor = self._connection.cursor()
        if status is None:
            sql = """SELECT id, name, description, priority, status, subproject_id
                     FROM Bugs WHERE subproject_id=? ORDER BY priority"""
            cursor.execute(sql, (subproject_id,))
        else:
            sql = f"""SELECT id, name, description, priority, status, subproject_id FROM Bugs
                      WHERE subproject_id=? AND status IN ({','.join(['?']*len(status))}) 
                      ORDER BY priority DESC, status"""
            cursor.execute(sql, (subproject_id,) + status)
        rows = cursor.fetchall()
        return list(map(bug_by_row, rows))

    def report_bug(self, name, subproject_id, description="", priority=0, status=0):
        cursor = self._connection.cursor()
        sql = """INSERT INTO Bugs (name, description, priority, status, subproject_id)
                 VALUES (?, ?, ?, ?, ?)"""
        cursor.execute(sql, (name, description, priority, status, subproject_id))
        self._connection.commit()

    def get_bug_id(self, subproject_id, bug_name):
        cursor = self._connection.cursor()
        sql = "SELECT id FROM Bugs WHERE subproject_id=? AND name=?;"
        cursor.execute(sql, (subproject_id, bug_name))
        bug_id = cursor.fetchone()[0]
        return bug_id

    def total_by_status(self, subproject_id, status=None):
        cursor = self._connection.cursor()
        if status is None:
            sql = "SELECT COUNT(id) FROM Bugs WHERE subproject_id=?;"
            cursor.execute(sql, (subproject_id,))
        else:
            sql = "SELECT COUNT(id) FROM Bugs WHERE subproject_id=? AND status=?;"
            cursor.execute(sql, (subproject_id, status))
        count = cursor.fetchone()[0]
        return count if count else 0

    def change_priority(self, bug_id, new_priority):
        cursor = self._connection.cursor()
        sql = "UPDATE Bugs SET priority=? WHERE id=?"
        cursor.execute(sql, (new_priority, bug_id))
        self._connection.commit()

    def change_status(self, bug_id, new_status):
        cursor = self._connection.cursor()
        sql = "UPDATE Bugs SET status=? WHERE id=?"
        cursor.execute(sql, (new_status, bug_id))
        self._connection.commit()

bug_repository = BugRepository(get_db_connection())
