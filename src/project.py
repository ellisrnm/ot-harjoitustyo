class Project:
    """Luo uuden projektin sovellukseen"""
    def __init__(self, name):
        self.name = name
        self.subprojects = []

    def create_subproject(self, name):
        self.subprojects.append(SubProject(name))

class SubProject:
    """Luo uuden aliprojektin"""
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Bug:
    """Luo uuden raportoidun virheen"""
    def __init__(self, name, description, priority):
        self.bug = name
        self.description = description
        self.priority = priority
