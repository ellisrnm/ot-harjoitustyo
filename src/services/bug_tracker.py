from repositories.project_repository import (project_repository as default_project_repository)
from repositories.subproject_repository import (subproject_repository as default_subproject_repository)
from repositories.bug_repository import (bug_repository as default_bug_repository)

class BugTrackerService:
    def __init__(
        self, 
        project_repository=default_project_repository,
        subproject_repository=default_subproject_repository,
        bug_repository=default_bug_repository
    ):
        self._project_repository = project_repository
        self._subproject_repository = subproject_repository
        self._bug_repository = bug_repository

    def get_id(self, project_name, subproject_name=None, bug_name=None):
        project_id = self._project_repository.get_project_id(project_name)
        if subproject_name:
            subproject_id = self._subproject_repository.get_subproject_id(project_id, subproject_name)
            if bug_name:
                bug_id = self._bug_repository.get_bug_id(subproject_id, bug_name)
                return bug_id
            else:
                return subproject_id
        else:
            return project_id

    def create_project(self, name):
        self._project_repository.create(name)

    def get_projects(self):
        projects_list = []
        projects = self._project_repository.fetch_all()
        for project in projects:
            projects_list.append(project.name)
        return projects_list

    def create_subproject(self, name, project_name):
        project_id = self.get_id(project_name)
        self._subproject_repository.create(name, project_id)

    def get_subprojects(self, project_name):
        subprojects_list = []
        project_id = self.get_id(project_name)
        subprojects = self._subproject_repository.fetch_all_from_project(project_id)
        for subproject in subprojects:
            subprojects_list.append(subproject.name)
        return subprojects_list

    def report_bug(self, project_name, subproject_name, bug_name):
        subproject_id = self.get_id(project_name, subproject_name)
        self._bug_repository.report_bug(bug_name, subproject_id)

    def get_bug_statistics(self, project_name, subproject_name):
        subproject_id = self.get_id(project_name, subproject_name)
        total = self._bug_repository.total_by_status(subproject_id)
        new = self._bug_repository.total_by_status(subproject_id, 0)
        under_development = self._bug_repository.total_by_status(subproject_id, 1)
        on_hold = self._bug_repository.total_by_status(subproject_id, 2)
        fixed = self._bug_repository.total_by_status(subproject_id, 3)
        current = total - fixed
        return (total, new, under_development, on_hold, fixed, current)

    def get_current_bugs_info(self, project_name, subproject_name):
        bugs_list = []
        subproject_id = self.get_id(project_name, subproject_name)
        bugs = self._bug_repository.fetch_all_from_subproject(subproject_id, (0,1,2))
        return bugs

    def get_current_bugs(self, project_name, subproject_name):
        bugs_list = []
        bugs = self.get_current_bugs_info(project_name, subproject_name)
        for bug in bugs:
                bugs_list.append(bug.name)
        return bugs_list

    def update_bug_status(self, project_name, subproject_name, bug_name, new_status):
        bug_id = self.get_id(project_name, subproject_name, bug_name)
        self._bug_repository.change_status(bug_id, new_status)
    
    def update_bug_priority(self, project_name, subproject_name, bug_name, new_priority):
        bug_id = self.get_id(project_name, subproject_name, bug_name)
        self._bug_repository.change_priority(bug_id, new_priority)

    def convert_priority(self, priority):
        priorities = {0: "Vähäinen", 1: "Normaali", 2: "Korkea"}
        if type(priority) == str:
            return list(priorities.values()).index(priority)
        elif type(priority) == int:
            return priorities[priority]

    def convert_status(self, status):
        statuses = {0: "Uusi", 1: "Kesken", 2: "Odottaa", 3: "Korjattu"}
        if type(status) == str:
            return list(statuses.values()).index(status)
        elif type(status) == int:
            return statuses[status]

bugtracker_service = BugTrackerService()