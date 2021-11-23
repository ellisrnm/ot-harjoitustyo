import unittest
from project import Project

class TestProject(unittest.TestCase):
    def setUp(self):
        self.project = Project("P1")

    def test_created_project_has_no_subprojects(self):
        self.assertEqual(self.project.subprojects,[])
