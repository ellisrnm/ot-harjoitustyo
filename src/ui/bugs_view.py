from tkinter import ttk, constants, StringVar, OptionMenu, IntVar
from services.bug_tracker import bugtracker_service

class BugView:
    def __init__(self, root, handle_subprojects, handle_bug_changes, project, subproject):
        self._root = root
        self._handle_subprojects = handle_subprojects
        self._handle_bug_changes = handle_bug_changes
        self._frame = None
        self._project = project
        self._subproject = subproject
        self._bug_chosen = StringVar(self._frame)
        self._status_chosen = StringVar(self._frame)
        self._priority_chosen = StringVar(self._frame)
        self._entry_bug = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def get_value(self):
        return self._project

    def get_project(self):
        return self._project
    
    def get_subproject(self):
        return self._subproject

    def _update_status_handler(self):
        new_status = self._status_chosen.get()
        bug = self._bug_chosen.get()
        status = bugtracker_service.convert_status(new_status)
        bugtracker_service.update_bug_status(self._project, self._subproject, bug, status)
        self._handle_bug_changes()

    def _update_priority_handler(self):
        new_priority = self._priority_chosen.get()
        bug = self._bug_chosen.get()
        priority = bugtracker_service.convert_priority(new_priority)
        bugtracker_service.update_bug_priority(self._project, self._subproject, bug, priority)
        self._handle_bug_changes()

    def _create_bug_handler(self):
        new_bug = self._entry_bug.get()
        bugtracker_service.report_bug(self._project, self._subproject, new_bug)
        self._handle_bug_changes()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        button_return = ttk.Button(
            master=self._frame,
            text="Palaa takaisin aliprojektinäkymään",
            command=self._handle_subprojects)
        button_return.pack(pady=(10, 10))

        title_page = ttk.Label(master=self._frame, text=f"Tarkastelet projektin {self._project} aliprojektia {self._subproject}", font='Arial 20 bold')
        total, new, under_development, on_hold, fixed, current = bugtracker_service.get_bug_statistics(self._project, self._subproject)
        label_totals = ttk.Label(master=self._frame, text=f"Bugeja yhteensä: {total}")
        label_totals_fixed = ttk.Label(master=self._frame, text=f"Korjattuja: {fixed}")
        label_totals_unfixed = ttk.Label(master=self._frame, text=f"Korjaamattomia: {current}")
        title_page.pack(pady=(10, 5))
        label_totals.pack(pady=(5, 0))
        label_totals_fixed.pack(pady=(0, 0))
        label_totals_unfixed.pack(pady=(0, 10))

        title_unfixed = ttk.Label(master=self._frame, text=f"Korjaamatta olevat bugit", font='Arial 20 bold')
        label_totals_new = ttk.Label(master=self._frame, text=f"Uusia: {new}")
        label_totals_develop = ttk.Label(master=self._frame, text=f"Keskeneräisiä: {under_development}")
        label_totals_hold = ttk.Label(master=self._frame, text=f"Odottavia: {on_hold}")
        title_unfixed.pack(pady=(10, 5))
        label_totals_new.pack(pady=(5, 0))
        label_totals_develop.pack(pady=(0, 0))
        label_totals_hold.pack(pady=(0, 10))

        bugs = bugtracker_service.get_current_bugs_info(self._project, self._subproject)
        if bugs:
            subtitle_bugs = ttk.Label(master=self._frame, text=f"Bugien tiedot", font='Arial 14 bold')
            subtitle_bugs.pack(pady=(10, 10))
            for bug in bugs:
                label_bug_info = ttk.Label(master=self._frame, 
                                      text=f"{bug.name}, Prioriteetti: {bugtracker_service.convert_priority(bug.priority)}, Tila: {bugtracker_service.convert_status(bug.status)}")
                label_bug_info.pack(pady=(0, 0))

        title_update = ttk.Label(master=self._frame, text=f"Muokkaa tietoja", font='Arial 20 bold')
        desc_update_1 = ttk.Label(master=self._frame, text="Voit muokata korjaamattamon bugin tilaa ja prioriteettia", font='Arial 14')
        desc_update_2 = ttk.Label(master=self._frame, text="Valitse alta bugi, jonka tietoja haluat muuttaa.", font='Arial 14')
        title_update.pack(pady=(20, 5))
        desc_update_1.pack(pady=(5, 0))
        desc_update_2.pack(pady=(0, 10))

        bug_options = bugtracker_service.get_current_bugs(self._project, self._subproject)
        if not bug_options:
            label_nobugs = ttk.Label(master=self._frame, text="Huom! Tällä aliprojektilla ei ole avoimia bugiraportteja")
            label_nobugs.pack(pady=(10, 10))
        else:
            self._bug_chosen.set(bug_options[0])
            choose = OptionMenu(self._frame, self._bug_chosen, *bug_options)
            choose.pack(pady=(10, 10))

            subtitle_update_status = ttk.Label(master=self._frame, text="Muuta tilastatus", font='Arial 14 bold')
            status_options = ["Uusi", "Kesken", "Odottaa", "Korjattu"]
            self._status_chosen.set(status_options[0])
            statuschoose = OptionMenu(self._frame, self._status_chosen, *status_options)
            statusbutton = ttk.Button(master=self._frame, text="Päivitä status", command=self._update_status_handler)
            subtitle_update_status.pack(pady=(10, 5))
            statuschoose.pack(pady=(5, 0))
            statusbutton.pack(pady=(0, 10))

            subtitle_update_priority = ttk.Label(master=self._frame, text="Muuta prioriteettia", font='Arial 14 bold')
            priority_options = ["Vähäinen", "Normaali", "Korkea"]
            self._priority_chosen.set(priority_options[0])
            prioritychoose = OptionMenu(self._frame, self._priority_chosen, *priority_options)
            prioritybutton = ttk.Button(master=self._frame, text="Päivitä prioriteetti", command=self._update_priority_handler)
            subtitle_update_priority.pack(pady=(10, 5))
            prioritychoose.pack(pady=(5, 0))
            prioritybutton.pack(pady=(0, 10))

        title_create_new = ttk.Label(master=self._frame, text=f"Luo uusi", font='Arial 20 bold')
        desc_create_new_1 = ttk.Label(master=self._frame, text="Voit lisätä uuden bugin kirjoittamalla sille nimen.", font='Arial 14')
        desc_create_new_2 = ttk.Label(master=self._frame, text="Nimi ei voi olla sama kuin jollain toisella raportoidulla bugilla.", font='Arial 14')
        self._entry_bug = ttk.Entry(master=self._frame)
        button_create_new = ttk.Button(master=self._frame, text="Raportoi", command=self._create_bug_handler)
        title_create_new.pack(pady=(10, 5))
        desc_create_new_1.pack(pady=(5, 0))
        desc_create_new_2.pack(pady=(0, 5))
        self._entry_bug.pack(pady=(5, 0))
        button_create_new.pack(pady=(0, 10))
