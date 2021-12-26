import unittest
from initialize_database import initialize_db
from services.bug_tracker import bugtracker_service

class TestBugTrackerService(unittest.TestCase):
    def setUp(self):
        initialize_db()

    def create_projects_works(self):
        bugtracker_service.create_project("Matin testiprojekti")
        bugtracker_service.create_project("Sonjan testiprojekti")
        self.assertEqual(len(bugtracker_service.get_projects()),2)
        bugtracker_service.create_project("Tiinan testiprojekti")
        self.assertEqual(len(bugtracker_service.get_projects()),3)

    def test_get_id_works(self):
        bugtracker_service.create_project("Tiinan testiprojekti")
        bugtracker_service.create_project("Matin testiprojekti")
        self.assertEqual(bugtracker_service.get_id("Matin testiprojekti"), 2)
        bugtracker_service.create_subproject("Sama nimi", "Tiinan testiprojekti")
        bugtracker_service.create_subproject("Sama nimi", "Matin testiprojekti")
        bugtracker_service.create_subproject("Random2", "Tiinan testiprojekti")
        bugtracker_service.create_subproject("Testiprojektin aliprojekti 2", "Matin testiprojekti")
        self.assertEqual(bugtracker_service.get_id("Matin testiprojekti", "Sama nimi"), 2)
        self.assertEqual(bugtracker_service.get_id("Matin testiprojekti", "Testiprojektin aliprojekti 2"), 4)
        bugtracker_service.report_bug("Matin testiprojekti", "Sama nimi", "Bug1")
        bugtracker_service.report_bug("Tiinan testiprojekti", "Sama nimi", "Bug1")
        self.assertEqual(bugtracker_service.get_id("Tiinan testiprojekti", "Sama nimi", "Bug1"), 2)
        self.assertEqual(bugtracker_service.get_id("Matin testiprojekti", "Sama nimi", "Bug1"), 1)

    def test_get_projects(self):
        bugtracker_service.create_project("Matin testiprojekti")
        bugtracker_service.create_project("Sonjan testiprojekti")
        projects = bugtracker_service.get_projects()
        self.assertEqual(len(projects),2)
        self.assertEqual(bugtracker_service.get_projects()[1],"Sonjan testiprojekti")

    def test_get_subprojects(self):
        bugtracker_service.create_project("Matin testiprojekti")
        bugtracker_service.create_project("Tiinan testiprojekti")
        bugtracker_service.create_subproject("Random2", "Tiinan testiprojekti")
        bugtracker_service.create_subproject("Sama nimi", "Tiinan testiprojekti")
        bugtracker_service.create_subproject("Sama nimi", "Matin testiprojekti")
        bugtracker_service.create_subproject("Testiprojektin aliprojekti 2", "Tiinan testiprojekti")
        projects = bugtracker_service.get_subprojects("Tiinan testiprojekti")
        self.assertEqual(len(projects),3)
        self.assertIn("Testiprojektin aliprojekti 2", bugtracker_service.get_subprojects("Tiinan testiprojekti"))
        self.assertEqual(bugtracker_service.get_subprojects("Tiinan testiprojekti")[1],"Sama nimi")

    def test_get_bugs(self):
        bugtracker_service.create_project("Matin testiprojekti")
        bugtracker_service.create_project("Tiinan testiprojekti")
        bugtracker_service.create_subproject("Tiinan aliprojekti", "Tiinan testiprojekti")
        bugtracker_service.report_bug("Tiinan testiprojekti", "Tiinan aliprojekti", "Bugi1")
        bugtracker_service.report_bug("Tiinan testiprojekti", "Tiinan aliprojekti", "Bugi2")
        bugtracker_service.report_bug("Tiinan testiprojekti", "Tiinan aliprojekti", "Korjattu Bugi")
        bugtracker_service.update_bug_status("Tiinan testiprojekti", "Tiinan aliprojekti", "Bugi2", 3)
        bugs = bugtracker_service.get_current_bugs("Tiinan testiprojekti", "Tiinan aliprojekti")
        self.assertEqual(len(bugs),2)

    def test_change_bug_status(self):
        bugtracker_service.create_project("Tiinan testiprojekti")
        bugtracker_service.create_subproject("Tiinan aliprojekti", "Tiinan testiprojekti")
        bugtracker_service.report_bug("Tiinan testiprojekti", "Tiinan aliprojekti", "Bugi1")
        bugtracker_service.report_bug("Tiinan testiprojekti", "Tiinan aliprojekti", "Bugi2")
        total, new, _, _, fixed, _ = bugtracker_service.get_bug_statistics("Tiinan testiprojekti", "Tiinan aliprojekti")
        self.assertEqual(total, 2)
        self.assertEqual(new, 2)
        self.assertEqual(fixed, 0)
        bugtracker_service.update_bug_status("Tiinan testiprojekti", "Tiinan aliprojekti", "Bugi2", 3)
        total, new, _, _, fixed, _ = bugtracker_service.get_bug_statistics("Tiinan testiprojekti", "Tiinan aliprojekti")
        self.assertEqual(total, 2)
        self.assertEqual(new, 1)
        self.assertEqual(fixed, 1)

    def test_priority_conversion(self):
        self.assertEqual(bugtracker_service.convert_priority(2), "Korkea")
        self.assertEqual(bugtracker_service.convert_priority("Vähäinen"), 0)

    def test_status_conversion(self):
        self.assertEqual(bugtracker_service.convert_status(3), "Korjattu")
        self.assertEqual(bugtracker_service.convert_status("Odottaa"), 2)
