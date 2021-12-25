from tkinter import OptionMenu, ttk, StringVar, constants
from services.bug_tracker import bugtracker_service

class SubProjectView:
    def __init__(self, root, handle_projects, handle_create_subproject, handle_bugs, project):
        self._root = root
        self._handle_projects = handle_projects
        self._handle_create_subproject = handle_create_subproject
        self._handle_bugs = handle_bugs
        self._frame = None
        self._entry_subproject = None
        self._subproject_chosen = StringVar(self._frame)
        self._project = project
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _create_subproject_handler(self):
        name = self._entry_subproject.get()
        bugtracker_service.create_subproject(name, self._project)
        self._handle_create_subproject()

    def get_value(self):
        return self._subproject_chosen.get()

    def get_project(self):
        return self._project

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        button_return = ttk.Button(
            master=self._frame,
            text="Palaa takaisin projektinäkymään",
            command=self._handle_projects)
        button_return.pack(pady=(10, 10))

        title_page = ttk.Label(master=self._frame,
        text=f"Tarkastelet projektia {self._project}",
        font='Arial 20 bold')

        desc_page_1 = ttk.Label(master=self._frame,
        text="Voit tarkastella olemassa olevia aliprojekteja tai luoda uuden aliprojektin.")

        desc_page_2 = ttk.Label(master=self._frame,
        text="Palaa takaisin projektinäkymään ylläolevasta napista.")

        title_page.pack(pady=(10, 5))
        desc_page_1.pack(pady=(5, 0))
        desc_page_2.pack(pady=(0, 10))

        title_open_subproject = ttk.Label(master=self._frame,
        text="Avaa aliprojekti",
        font='Arial 20 bold')

        desc_open_subproject = ttk.Label(master=self._frame,
        text="Valitse alta aliprojekti, jota haluat tarkastella.",
        font='Arial 14')

        title_open_subproject.pack(pady=(10, 5))
        desc_open_subproject.pack(pady=(5, 10))

        subproject_options = bugtracker_service.get_subprojects(self._project)
        if not subproject_options:
            label_no_subprojects = ttk.Label(master=self._frame,
            text="Huom! Tällä projektilla ei ole vielä aliprojekteja")
            label_no_subprojects.pack(pady=(10, 10))
        else:
            self._subproject_chosen.set(subproject_options[0])
            manu_subprojects = OptionMenu(self._frame, self._subproject_chosen, *subproject_options)
            button_show_project = ttk.Button(
                master=self._frame,
                text="Näytä valittu aliprojekti",
                command=self._handle_bugs)
            manu_subprojects.pack(pady=(10, 0))
            button_show_project.pack(pady=(0, 10))

        title_new_subproject = ttk.Label(master=self._frame,
        text="Luo uusi aliprojekti",
        font='Arial 20 bold')

        desc_new_subproject_1 = ttk.Label(master=self._frame,
        text="Voit luoda uuden aliprojektin tälle projektille kirjoittamalla sille nimen.",
        font='Arial 14')

        desc_new_subproject_2 = ttk.Label(master=self._frame,
        text="Nimi ei voi olla sama kuin jollain toisella aliprojektilla.",
        font='Arial 14')

        self._entry_subproject = ttk.Entry(master=self._frame)
        button_new_subproject = ttk.Button(master=self._frame,
        text="Luo",
        command=self._create_subproject_handler)

        title_new_subproject.pack(pady=(10, 5))
        desc_new_subproject_1.pack(pady=(5, 0))
        desc_new_subproject_2.pack(pady=(0, 5))
        self._entry_subproject.pack(pady=(5, 0))
        button_new_subproject.pack(pady=(0, 10))
