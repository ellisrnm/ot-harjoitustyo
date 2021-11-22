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
            else:
                print("Komento ei käytössä")

app = BugTrackerApp()
app.start()