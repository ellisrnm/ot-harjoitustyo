from tkinter import OptionMenu, ttk, StringVar, constants
from services.bug_tracker import bugtracker_service

class ProjectView:
    def __init__(self, root, handle_subprojects, handle_create_project):
        self._root = root
        self._handle_subprojects = handle_subprojects
        self._handle_create_project = handle_create_project
        self._entry_project = None
        self._frame = None
        self._project_chosen = StringVar(self._frame)
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def get_value(self):
        return self._project_chosen.get()

    def _create_project_handler(self):
        name = self._entry_project.get()
        bugtracker_service.create_project(name)
        self._handle_create_project()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        title_app = ttk.Label(master=self._frame, text="Bugiseurantasovellus", font='Arial 20 bold')
        desc_app_1 = ttk.Label(master=self._frame, text="Sovellukseen voi raportoida eri projekteista löytyneitä virheitä tai puutteita.")
        desc_app_2 = ttk.Label(master=self._frame, text="Sovelluksen tarkoituksena on toimia apuna virheiden tilan seurannassa.")
        desc_app_3 = ttk.Label(master=self._frame, text="Voit tarkastella olemassa olevia projekteja tai luo uuden projektin.")
        title_app.pack(pady=(10, 5))
        desc_app_1.pack(pady=(5, 0))
        desc_app_2.pack(pady=(0, 0))
        desc_app_3.pack(pady=(0, 10))

        title_open_project = ttk.Label(master=self._frame, text="Avaa projekti", font='Arial 20 bold')
        desc_open_project = ttk.Label(master=self._frame, text="Valitse alta projekti, jota haluat tarkastella.", font='Arial 14')
        title_open_project.pack(pady=(10, 5))
        desc_open_project.pack(pady=(5, 10))

        project_options = bugtracker_service.get_projects()
        if not project_options:
            label_no_projects = ttk.Label(master=self._frame, text="Huom! Tässä sovelluksessa ei ole vielä projekteja")
            label_no_projects.pack(pady=(10, 10))
        else:
            self._project_chosen.set(project_options[0])
            menu_projects = OptionMenu(self._frame, self._project_chosen, *project_options)
            button_show_project = ttk.Button(
                master=self._frame,
                text="Näytä valittu projekti",
                command=self._handle_subprojects)
            menu_projects.pack(pady=(10, 0))
            button_show_project.pack(pady=(0, 10))

        title_new_project = ttk.Label(master=self._frame, text="Luo uusi projekti", font='Arial 20 bold')
        desc_new_project_1 = ttk.Label(master=self._frame, text="Voit luoda uuden projektin kirjoittamalla sille nimen.", font='Arial 14')
        desc_new_project_2 = ttk.Label(master=self._frame, text="Nimi ei voi olla sama kuin jollain toisella projektilla.", font='Arial 14')
        self._entry_project = ttk.Entry(master=self._frame)
        button_new_project = ttk.Button(master=self._frame, text="Luo", command=self._create_project_handler)

        title_new_project.pack(pady=(10, 5))
        desc_new_project_1.pack(pady=(5, 0))
        desc_new_project_2.pack(pady=(0, 5))
        self._entry_project.pack(pady=(5, 0))
        button_new_project.pack(pady=(0, 10))