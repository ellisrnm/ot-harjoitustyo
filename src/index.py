from repositories.bug_repository import bug_repository
from repositories.project_repository import project_repository
from repositories.subproject_repository import subproject_repository

class BugTrackerApp():
    def __init__(self):
        pass

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
                project_id = project_repository.get_project_id(project_name)
                for subproject in subproject_repository.fetch_all_from_project(project_id):
                    print(subproject.name)
            elif command == "4":
                project_name = input("Valitse ensin projekti: ")
                project_id = project_repository.get_project_id(project_name)
                subproject_name = input("Nimeä aliprojekti: ")
                subproject_repository.create(subproject_name, project_id)
            elif command == "5":
                project_name = input("Valitse ensin projekti: ")
                project_id = project_repository.get_project_id(project_name)
                subproject_name = input("Valitse vielä aliprojekti: ")
                subproject_id = subproject_repository.get_subproject_id(project_id, subproject_name)
                for bug in bug_repository.fetch_all_from_subproject(subproject_id):
                    print(bug.status, ',', bug.priority, ':', bug.name, bug.description)
            elif command == "6":
                project_name = input("Valitse ensin projekti: ")
                project_id = project_repository.get_project_id(project_name)
                subproject_name = input("Valitse vielä aliprojekti: ")
                subproject_id = subproject_repository.get_subproject_id(project_id, subproject_name)
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
                            bug_priority = 3
                        elif bug_priority == "M":
                            bug_priority = 2
                        elif bug_priority == "H":
                            bug_priority = 1
                        break
                    else:
                        print("Syöte ei kelpaa")
                bug_repository.report_bug(bug_name, subproject_id, bug_desc, bug_priority)
            elif command == "7":
                project_name = input("Valitse ensin projekti: ")
                project_id = project_repository.get_project_id(project_name)
                subproject_name = input("Valitse vielä aliprojekti: ")
                subproject_id = subproject_repository.get_subproject_id(project_id, subproject_name)
                bug_name = input("Valitse bugin nimi:")
                print("Valitse prioriteetti")
                print("L: Low")
                print("M: Medium")
                print("H: High")
                while True:
                    new_priority = input("Anna bugin uusi prioriteetti: ")
                    if new_priority in ("L","M","H"):
                        if new_priority == "L":
                            new_priority = 3
                        elif new_priority == "M":
                            new_priority = 2
                        elif new_priority == "H":
                            new_priority = 1
                        break
                    else:
                        print("Syöte ei kelpaa")
                bug_id = bug_repository.get_bug_id(subproject_id, bug_name)
                bug_repository.change_priority(bug_id, new_priority)
            else:
                print("Komento ei käytössä")

app = BugTrackerApp()
app.start()