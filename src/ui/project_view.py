from tkinter import OptionMenu, ttk, StringVar, constants

class ProjectView:
    def __init__(self, root, handle_subprojects):
        self._root = root
        self._handle_subprojects = handle_subprojects
        self._frame = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def get_value(self):
        return self.variable.get()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        title = ttk.Label(master=self._frame, text="Tervetuloa sovellukseen!", font='Arial 20 bold')

        subtitle = ttk.Label(master=self._frame, text="Voit tarkastella olemassa olevia projekteja tai luo uuden projektin")
        label1 = ttk.Label(master=self._frame, text="Valitse alta projekti, jota haluat tarkastella.", font='Arial 14 bold')
        OPTIONS = ["P1", "P2", "P3"]
        self.variable = StringVar(self._frame)
        self.variable.set(OPTIONS[0])
        choose = OptionMenu(self._frame, self.variable, *OPTIONS)
        self.muuttuja = None
        button = ttk.Button(
            master=self._frame,
            text="Näytä valittu projekti",
            command=self._handle_subprojects
        )

        label2 = ttk.Label(master=self._frame, text="Voit luoda uuden projektin kirjoittamalla sille nimen", font='Arial 14 bold')
        entry = ttk.Entry(master=self._frame)
        button2 = ttk.Button(master=self._frame, text="Luo")

        title.pack(pady=(10, 10))
        subtitle.pack(pady=(0, 10))
        label1.pack(pady=(0, 10))
        choose.pack()
        button.pack()

        label2.pack(pady=(10, 10))
        entry.pack()
        button2.pack(pady=(0, 10))