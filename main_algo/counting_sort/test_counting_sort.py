import unittest

from test_case import test_case_sort_int, test_case_value_int
from counting_sort import counting_sort


class TestCountingSort(unittest.TestCase):
    def test_sort(self):
        for a in test_case_sort_int:
            self.assertEqual(counting_sort(a), sorted(a))

    def test_values(self):
        for a in test_case_value_int:
            self.assertRaises(TypeError, counting_sort, a)
