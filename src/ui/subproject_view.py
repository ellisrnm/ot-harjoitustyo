from tkinter import OptionMenu, ttk, StringVar, constants

class SubProjectView:
    def __init__(self, root, handle_projects, handle_bugs, project):
        self._root = root
        self._handle_projects = handle_projects
        self._handle_bugs = handle_bugs
        self._frame = None
        self._project = project
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def get_value(self):
        return self.variable.get()

    def get_project(self):
        return self._project

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        returnbutton = ttk.Button(
            master=self._frame,
            text="Palaa takaisin projektinäkymään",
            command=self._handle_projects
        )

        title = ttk.Label(master=self._frame, text=f"Tarkastelet projektia {self._project}", font='Arial 20 bold')

        subtitle = ttk.Label(master=self._frame, text="Voit tarkastella olemassa olevia aliprojekteja tai luoda uuden aliprojektin")
        label1 = ttk.Label(master=self._frame, text="Valitse alta aliprojekti, jota haluat tarkastella.", font='Arial 14 bold')
        OPTIONS = ["SP1", "SP2", "SP3"]
        self.variable = StringVar(self._frame)
        self.variable.set(OPTIONS[0])
        choose = OptionMenu(self._frame, self.variable, *OPTIONS)
        button = ttk.Button(
            master=self._frame,
            text="Näytä valittu aliprojekti",
            command=self._handle_bugs
        )

        label2 = ttk.Label(master=self._frame, text="Voit luoda uuden aliprojektin kirjoittamalla sille nimen", font='Arial 14 bold')
        entry = ttk.Entry(master=self._frame)
        button2 = ttk.Button(master=self._frame, text="Luo")

        returnbutton.pack(pady=(10, 10))
        title.pack(pady=(10, 10))

        title.pack(pady=(10, 10))
        subtitle.pack(pady=(0, 10))
        label1.pack(pady=(0, 10))
        choose.pack()
        button.pack()

        label2.pack(pady=(10, 10))
        entry.pack()
        button2.pack(pady=(0, 10))