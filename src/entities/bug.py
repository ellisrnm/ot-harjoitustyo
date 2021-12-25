class Bug:
    """Luo uuden raportoidun virheen"""
    def __init__(self, bug_id, name, description, priority, status, subproject_id):
        self.bug_id = bug_id
        self.name = name
        self.description = description
        self.priority = priority
        self.status = status
        self.subproject_id = subproject_id
