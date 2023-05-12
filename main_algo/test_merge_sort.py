import unittest

from test_case import test_case_sort, test_case_value
from merge_sort import merge_sort


class TestMergeSort(unittest.TestCase):
    def test_merge_sort(self):
        for a in test_case_sort:
            self.assertEqual(merge_sort(a), sorted(a))

    def test_values(self):
        for a in test_case_value:
            self.assertRaises(TypeError, merge_sort, a)
