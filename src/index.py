from project import Project

class BugTrackerApp():
    def __init__(self):
        self.__projects = []

    def create_project(self, name):
        self.__projects.append(Project(name))

    def start(self):

        print("Tervetuloa sovellukseen")
        print("Komennot")
        print("0: Lopetus")
        print("1: Tulosta nykyiset projektit")
        print("2: Luo uusi projekti")
        print("3: Tulosta projektin aliprojektit")
        print("4: Luo uusi aliprojekti")
        print("5: Raportoi uusi bugi")

        while True:
            print("")
            command = input("Valitse komento: ")
            if command == "0":
                break
            elif command == "1":
                for project in self.__projects:
                    print(project.name)
            elif command == "2":
                project_name = input("Nimeä projekti: ")
                self.create_project(project_name)
            elif command == "3":
                project_name = input("Valitse ensin projekti: ")
                for project in self.__projects:
                    if project.name==project_name:
                        for subproject in project.subprojects:
                            print(subproject.name)
            elif command == "4":
                project_name = input("Valitse ensin projekti: ")
                subproject_name = input("Nimeä aliprojekti: ")
                for project in self.__projects:
                    if project.name==project_name:
                        project.create_subproject(subproject_name)
            elif command == "5":
                project_name = input("Valitse ensin projekti: ")
                subproject_name = input("Valitse vielä aliprojekti: ")
                bug_name = input("Nimeä löytynyt bugi: ")
                for project in self.__projects:
                    if project.name==project_name:
                        for subproject in project.subprojects:
                            if subproject.name==subproject_name:
                                subproject.report_bug(bug_name)
            else:
                print("Komento ei käytössä")

app = BugTrackerApp()
app.start()