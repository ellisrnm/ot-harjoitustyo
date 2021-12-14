import unittest
from initialize_database import initialize_db
from repositories.project_repository import project_repository

class TestProjectRepository(unittest.TestCase):
    def setUp(self):
        initialize_db()

    def test_project_is_created(self):
        project_repository.create('Project_1')
        projects = project_repository.fetch_all()
        self.assertEqual(len(projects), 1)

    def test_project_information_created_correctly(self):
        project_repository.create('Project_1')
        project = project_repository.fetch_all()[0]
        self.assertEqual(project.id, 1)
        self.assertEqual(project.name, 'Project_1')

    def test_project_id_is_fetched_correctly(self):
        project_repository.create('Project_a')
        project_repository.create('Project_b')
        project_repository.create('Project c')
        self.assertEqual(project_repository.get_project_id('Project_a'), 1)
        self.assertEqual(project_repository.get_project_id('Project_b'), 2)
        self.assertEqual(project_repository.get_project_id('Project c'), 3)