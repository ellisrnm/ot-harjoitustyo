class Project:
    """Luo uuden projektin sovellukseen"""
    def __init__(self, name):
        self.name = name
        self.subprojects = []

    def create_subproject(self, name):
        self.subprojects.append(SubProject(name))

class SubProject:
    """Luo uuden aliprojektin"""
    def __init__(self, name, description=""):
        self.name = name
        self.description = description
        self.bugs = []

    def report_bug(self, name, description="", priority="Low", status="New"):
        self.bugs.append(Bug(name, description, priority, status))

    def change_bug_priority(self, name, new_priority):
        for bug in self.bugs:
            if bug.name == name:
                bug.priority = new_priority

class Bug:
    """Luo uuden raportoidun virheen"""
    def __init__(self, name, description, priority, status):
        self.name = name
        self.description = description
        self.priority = priority
        self.status = status
