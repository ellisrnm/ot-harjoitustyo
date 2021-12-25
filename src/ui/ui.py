from tkinter import Tk
from ui.project_view import ProjectView
from ui.subproject_view import SubProjectView
from ui.bugs_view import BugView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_projects_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _show_projects_view(self):
        self._hide_current_view()
        self._current_view = ProjectView(
            self._root,
            self._handle_subprojects,
            self._handle_new_project
        )
        self._current_view.pack()

    def _show_subprojects_view(self, project_name=None):
        if not project_name:
            self._project_name = self._current_view.get_value()
        else: 
            self._project_name = project_name
        self._hide_current_view()
        self._current_view = SubProjectView(
            self._root,
            self._handle_projects,
            self._handle_new_subproject,
            self._handle_bugs,
            self._project_name
        )
        self._current_view.pack()

    def _show_bugs_view(self, project_name=None, subproject_name=None):
        if not project_name:
            self._project_name = self._current_view.get_project()
            self._subproject_name = self._current_view.get_value()
        else: 
            self._project_name = project_name
            self._subproject_name = subproject_name
        self._hide_current_view()
        self._current_view = BugView(
            self._root,
            self._handle_subprojects,
            self._handle_bug_changes,
            self._project_name,
            self._subproject_name
        )
        self._current_view.pack()

    def _handle_new_project(self):
        self._show_projects_view()

    def _handle_new_subproject(self):
        self._project_name = self._current_view.get_project()
        self._show_subprojects_view(self._project_name)

    def _handle_bug_changes(self):
        self._project_name = self._current_view.get_project()
        self._subproject_name = self._current_view.get_subproject()
        self._show_bugs_view(self._project_name, self._subproject_name)

    def _handle_projects(self):
        self._show_projects_view()

    def _handle_subprojects(self):
        self._show_subprojects_view()

    def _handle_bugs(self):
        self._show_bugs_view()