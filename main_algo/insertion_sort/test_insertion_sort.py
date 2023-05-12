import unittest

from test_case import test_case_sort, test_case_value
from insertion_sort import insertion_sort


class TestInsertionSort(unittest.TestCase):
    def test_sort(self):
        for a in test_case_sort:
            self.assertEqual(insertion_sort(a), sorted(a))

    def test_values(self):
        for a in test_case_value:
            self.assertRaises(TypeError, insertion_sort, a)
