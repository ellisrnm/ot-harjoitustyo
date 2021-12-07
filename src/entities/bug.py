from repositories.subproject_repository import subproject_by_row


class Bug:
    """Luo uuden raportoidun virheen"""
    def __init__(self, id, name, description, priority, status, subproject_id):
        self.id = id
        self.name = name
        self.description = description
        self.priority = priority
        self.status = status
        self.subproject_id = subproject_id

    def priority(self):
        if self.priority == 3:
            return "Low"
        elif self.priority == 2:
            return "Medium"
        elif self.priority == 1:
            return "High"