import unittest

from test_case import test_case_sort_int, test_case_value_int
from radix_sort import radix_sort


class TestRadixSort(unittest.TestCase):
    def test_sort(self):
        for a in test_case_sort_int:
            self.assertEqual(radix_sort(a), sorted(a))

    def test_values(self):
        for a in test_case_value_int:
            self.assertRaises(TypeError, radix_sort, a)
