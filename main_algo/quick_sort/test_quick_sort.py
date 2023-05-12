import unittest

from test_case import test_case_sort, test_case_value
from quick_sort import quick_sort


class TestQuickSort(unittest.TestCase):
    def test_quick_sort(self):
        for a in test_case_sort:
            self.assertEqual(quick_sort(a), sorted(a))

    def test_values(self):
        for a in test_case_value:
            self.assertRaises(TypeError, quick_sort, a)
