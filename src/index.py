#from project import Project
from initialize_database import initialize_db
from repositories.project_repository import project_repository
from repositories.subproject_repository import subproject_repository

class BugTrackerApp():
    def __init__(self):
        initialize_db()
    #    self.__projects = []

    #def create_project(self, name):
    #    self.__projects.append(Project(name))

    def start(self):

        print("Tervetuloa sovellukseen")
        print("Komennot")
        print("0: Lopetus")
        print("1: Tulosta nykyiset projektit")
        print("2: Luo uusi projekti")
        print("3: Tulosta projektin aliprojektit")
        print("4: Luo uusi aliprojekti")
        print("5: Tulosta aliprojektin bugit")
        print("6: Raportoi uusi bugi")
        print("7: Vaihda bugin prioriteettia")

        while True:
            print("")
            command = input("Valitse komento: ")
            if command == "0":
                break
            elif command == "1":
                for project in project_repository.fetch_all():
                    print(project.name)
            elif command == "2":
                project_name = input("Nimeä projekti: ")
                project_repository.create(project_name)
            elif command == "3":
                project_name = input("Valitse ensin projekti: ")
                for project in project_repository.fetch_all():
                    if project.name==project_name:
                        for subproject in subproject_repository.fetch_all_from_project(project.id):
                            print(subproject.name)
            elif command == "4":
                project_name = input("Valitse ensin projekti: ")
                subproject_name = input("Nimeä aliprojekti: ")
                for project in project_repository.fetch_all():
                    if project.name==project_name:
                        subproject_repository.create(subproject_name)
            elif command == "5":
                project_name = input("Valitse ensin projekti: ")
                subproject_name = input("Valitse vielä aliprojekti: ")
                for project in project_repository.fetch_all():
                    if project.name==project_name:
                        for subproject in subproject_repository.fetch_all_from_project(project.id):
                            if subproject.name==subproject_name:
                                for bug in subproject.bugs:
                                    print(bug.status, ',', bug.priority, ':', bug.name, bug.description)
            elif command == "6":
                project_name = input("Valitse ensin projekti: ")
                subproject_name = input("Valitse vielä aliprojekti: ")
                bug_name = input("Nimeä löytynyt bugi: ")
                bug_desc = input("Kuvaile löytynyttä bugia: ")
                print("Valitse prioriteetti")
                print("L: Low")
                print("M: Medium")
                print("H: High")
                while True:
                    bug_priority = input("Anna bugin prioriteetti: ")
                    if bug_priority in ("L","M","H"):
                        if bug_priority == "L":
                            bug_priority = "Low"
                        elif bug_priority == "M":
                            bug_priority = "Medium"
                        elif bug_priority == "H":
                            bug_priority = "High"
                        break
                    else:
                        print("Syöte ei kelpaa")
                for project in self.__projects:
                    if project.name==project_name:
                        for subproject in project.subprojects:
                            if subproject.name==subproject_name:
                                subproject.report_bug(bug_name, bug_desc, bug_priority)
            elif command == "7":
                project_name = input("Valitse ensin projekti: ")
                subproject_name = input("Valitse vielä aliprojekti: ")
                bug_name = input("Valitse bugin nimi:")
                print("Valitse prioriteetti")
                print("L: Low")
                print("M: Medium")
                print("H: High")
                while True:
                    new_priority = input("Anna bugin uusi prioriteetti: ")
                    if new_priority in ("L","M","H"):
                        if new_priority == "L":
                            new_priority = "Low"
                        elif new_priority == "M":
                            new_priority = "Medium"
                        elif new_priority == "H":
                            new_priority = "High"
                        break
                    else:
                        print("Syöte ei kelpaa")
                for project in self.__projects:
                    if project.name==project_name:
                        for subproject in project.subprojects:
                            if subproject.name==subproject_name:
                                subproject.sort_bug_list()
                                subproject.change_bug_priority(bug_name, new_priority)
            else:
                print("Komento ei käytössä")

app = BugTrackerApp()
app.start()