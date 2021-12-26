import unittest
from initialize_database import initialize_db
from repositories.bug_repository import bug_repository

class TestSubProjectRepository(unittest.TestCase):
    def setUp(self):
        initialize_db()

    def test_bug_is_created(self):
        bug_repository.report_bug("Bug1", 1)
        bug_repository.report_bug("Bug2", 1)
        bug_repository.report_bug("Bug1", 2)
        bugs = bug_repository.fetch_all_from_subproject(1)
        self.assertEqual(len(bugs), 2)

    def test_bug_information_created_correctly(self):
        bug_repository.report_bug("Bug1", 3)
        bug_1 = bug_repository.fetch_all_from_subproject(3)[0]
        self.assertEqual(bug_1.bug_id, 1)
        self.assertEqual(bug_1.name, "Bug1")
        self.assertEqual(bug_1.description, "")
        self.assertEqual(bug_1.priority, 0)
        self.assertEqual(bug_1.status,0)
        self.assertEqual(bug_1.subproject_id, 3)

    def test_bug_id_is_fetched_correctly(self):
        bug_repository.report_bug("Bug1", 3)
        bug_repository.report_bug("Bug2", 1)
        bug_repository.report_bug("Bug3", 3)
        self.assertEqual(bug_repository.get_bug_id(3, "Bug3"), 3)

    def test_fetching_bugs_by_status(self):
        bug_repository.report_bug("Bug1", 1)
        bug_repository.report_bug("Bug2", 1)
        bug_repository.report_bug("Bug3", 1)
        bug_repository.report_bug("Bug4", 1)
        bug_repository.report_bug("Bug5", 1)
        bug_repository.report_bug("Bug6", 2)
        bug_repository.change_status(1,3)
        bug_repository.change_status(2,1)
        bug_repository.change_status(3,1)
        bug_repository.change_status(4,2)
        self.assertEqual(len(bug_repository.fetch_all_from_subproject(1,(1,))),2)
        self.assertEqual(len(bug_repository.fetch_all_from_subproject(1,(1,2))),3)
        self.assertEqual(len(bug_repository.fetch_all_from_subproject(1)),5)

    def test_change_priority_works(self):
        bug_repository.report_bug("Bug1", 3)
        bug_1 = bug_repository.fetch_all_from_subproject(3)[0]
        self.assertEqual(bug_1.priority,0)
        bug_repository.change_priority(1,2)
        bug_1 = bug_repository.fetch_all_from_subproject(3)[0]
        self.assertEqual(bug_1.priority,2)

    def test_change_status_works(self):
        bug_repository.report_bug("Bug1", 3)
        bug_1 = bug_repository.fetch_all_from_subproject(3)[0]
        self.assertEqual(bug_1.status,0)
        bug_repository.change_status(1,3)
        bug_1 = bug_repository.fetch_all_from_subproject(3)[0]
        self.assertEqual(bug_1.status,3)

    def test_total_by_status_is_correct(self):
        bug_repository.report_bug("Bug1", 1)
        bug_repository.report_bug("Bug2", 1)
        bug_repository.report_bug("Bug3", 1)
        bug_repository.report_bug("Bug4", 1)
        bug_repository.report_bug("Bug5", 1)
        bug_repository.report_bug("Bug6", 2)
        bug_repository.change_status(1,3)
        bug_repository.change_status(2,1)
        bug_repository.change_status(3,1)
        bug_repository.change_status(4,2)
        self.assertEqual(bug_repository.total_by_status(1),5)
        self.assertEqual(bug_repository.total_by_status(1,1),2)