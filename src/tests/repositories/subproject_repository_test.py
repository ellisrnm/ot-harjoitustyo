import unittest
from initialize_database import initialize_db
from repositories.subproject_repository import subproject_repository

class TestSubProjectRepository(unittest.TestCase):
    def setUp(self):
        initialize_db()

    def test_project_is_created(self):
        subproject_repository.create("Subproject_1", 1)
        subproject_repository.create("Subproject_2", 1)
        subproject_repository.create("Subproject_1", 2)
        subprojects = subproject_repository.fetch_all_from_project(1)
        self.assertEqual(len(subprojects), 2)

    def test_project_information_created_correctly(self):
        subproject_repository.create("Subproject_1", 1)
        subproject_1 = subproject_repository.fetch_all_from_project(1)[0]
        self.assertEqual(subproject_1.id, 1)
        self.assertEqual(subproject_1.name, "Subproject_1")
        self.assertEqual(subproject_1.description, "")
        subproject_repository.create("Subproject_2", 2, "error")
        subproject_2 = subproject_repository.fetch_all_from_project(2)[0]
        self.assertEqual(subproject_2.id, 2)
        self.assertEqual(subproject_2.name, "Subproject_2")
        self.assertEqual(subproject_2.description, "error")

    def test_fetching_from_right_project(self):
        subproject_repository.create("Subproject_1", 1)
        subproject_repository.create("Subproject_2", 1)
        subproject_repository.create("Subproject_a", 1)
        subproject_repository.create("Subproject_1", 2)
        subproject_repository.create("Subproject_a", 3)
        subproject_repository.create("Subproject_b", 3)
        subproject_repository.create("Subproject  c", 3)
        subproject_repository.create("1", 3)
        self.assertEqual(len(subproject_repository.fetch_all_from_project(1)), 3)
        self.assertEqual(len(subproject_repository.fetch_all_from_project(2)), 1)
        self.assertEqual(len(subproject_repository.fetch_all_from_project(3)), 4)

    def test_project_id_is_fetched_correctly(self):
        subproject_repository.create('sp_a', 1, "aa")
        subproject_repository.create('sp b', 1, "bb")
        subproject_repository.create('sp_a', 2, "aa")
        self.assertEqual(subproject_repository.get_subproject_id(1, 'sp_a'), 1)
        self.assertEqual(subproject_repository.get_subproject_id(2, 'sp_a'), 3)
        self.assertEqual(subproject_repository.get_subproject_id(1, 'sp b'), 2)
    