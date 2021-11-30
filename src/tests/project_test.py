import unittest
from project import Project, SubProject, Bug

class TestProject(unittest.TestCase):
    def setUp(self):
        self.project = Project("P1")

    def test_created_project_has_no_subprojects(self):
        self.assertEqual(self.project.subprojects,[])

    def test_creating_subproject_increases_subproject_list_length(self):
        self.project.create_subproject('P_SP1')
        self.assertEqual(len(self.project.subprojects),1)

class TestSubProject(unittest.TestCase):
    def setUp(self):
        self.subproject = SubProject("SP1")

    def test_created_project_has_no_reported_bugs(self):
        self.assertEqual(self.subproject.bugs,[])

    def test_reporting_bugs_increases_bug_list_length(self):
        self.subproject.report_bug("BUG1")
        self.subproject.report_bug("BUG2")
        self.assertEqual(len(self.subproject.bugs),2)

class TestBug(unittest.TestCase):
    def setUp(self):
        self.bug = Bug("New bug", "Missing data", "Low")