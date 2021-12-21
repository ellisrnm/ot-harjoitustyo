from tkinter import ttk, constants

class BugView:
    def __init__(self, root, handle_subprojects, project, subproject):
        self._root = root
        self._handle_subprojects = handle_subprojects
        self._frame = None
        self._project = project
        self._subproject = subproject
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def get_value(self):
        return self._project

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        returnbutton = ttk.Button(
            master=self._frame,
            text="Palaa takaisin aliprojektinäkymään",
            command=self._handle_subprojects
        )

        title = ttk.Label(master=self._frame, text=f"Tarkastelet aliprojektia {self._subproject}", font='Arial 20 bold')

        returnbutton.pack(pady=(10, 10))
        title.pack(pady=(10, 10))
