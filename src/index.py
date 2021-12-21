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
            self._handle_subprojects
        )
        self._current_view.pack()

    def _show_subprojects_view(self):
        self._arvo = self._current_view.get_value()
        self._hide_current_view()
        self._current_view = SubProjectView(
            self._root,
            self._handle_projects,
            self._handle_bugs,
            self._arvo
        )
        self._current_view.pack()

    def _show_bugs_view(self):
        self._arvo = self._current_view.get_value()
        self._project = self._current_view.get_project()
        self._hide_current_view()
        self._current_view = BugView(
            self._root,
            self._handle_subprojects,
            self._project,
            self._arvo
        )
        self._current_view.pack()

    def _handle_projects(self):
        self._show_projects_view()

    def _handle_subprojects(self):
        self._show_subprojects_view()

    def _handle_bugs(self):
        self._show_bugs_view()

window = Tk()
window.title("Bugiseurantasovellus")

ui = UI(window)
ui.start()

window.mainloop()