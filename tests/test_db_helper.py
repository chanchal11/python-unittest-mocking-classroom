from unittest import TestCase
from unittest.mock import patch
from src.db_helper import DbHelper


class TestDBHelper(TestCase):
    def setUp(self):
        self.db_helper = DbHelper

    @patch('src.db_helper.DbHelper')
    def test_get_min_salary(self, MockDBHelper):
        db_helper = MockDBHelper()
        db_helper.get_min_salary.return_value = 10000
        actual = db_helper.get_min_salary()
        expected = 10000
        self.assertEqual(expected, actual)

    @patch('src.db_helper.DbHelper')
    def test_get_max_salary(self, MockDBHelper):
        db_helper = MockDBHelper()
        db_helper.get_max_salary.return_value = 10000
        actual = db_helper.get_max_salary()
        expected = 10000
        self.assertEqual(expected, actual)

