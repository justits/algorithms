import sys
import unittest
import random

from k_order_statistic import k_order_statistic

test_case_find = [
    ([0], 0, 0),
    ([-1, -1, -1, -1], 3, -1),
    ([-1, -1, -1, -1], 1, -1),
    ([-1, 0, 3, -10], 3, 3),
    ([-1, -2, -3, -4, -5], 0, -5),
    ([1, 2, 3, 4, 5], 1, 2),
    ([True, False, True], 2, True),
    ([sys.maxsize], 0, sys.maxsize),
    ([True, 10], 1, 10)
]

test_case_value = [
    [],
    [1, 'a', None, True],
    ['asd', True]
]


class TestKOrderStatistic(unittest.TestCase):

    def test_find(self):
        for a, k, ans in test_case_find:
            self.assertEqual(k_order_statistic(a, k), ans)

    def test_values(self):
        for a in test_case_value:
            self.assertRaises(TypeError, k_order_statistic, (a, random.randint(0, 10)))

        for a, k, ans in test_case_find:
            self.assertRaises(TypeError, k_order_statistic, (a, k + len(a)))
