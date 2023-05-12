import sys

test_case_sort = [
    [],
    [-1, -1, -1, -1],
    [0],
    ['t', 'a', 'v', 'r', 'z'],
    [1, 2, 3, 4, 5],
    [-1, -2, -3, -4, -5],
    [1.1, 1],
    [float('inf')],
    [float('-inf')],
    [sys.maxsize],
    [sys.maxsize - 10, sys.maxsize, sys.maxsize - 2],
    [True, False, True],
    [None],
    [True, 10],
    ['test', 'c']
]

test_case_value = [
    [1, 'a', None, True],
    ['asd', True]
]

test_case_sort_int = [
    [],
    [-1, -1, -1, -1],
    [0],
    [3, 2, 1],
    [-1, -2, -3, -4, -5],
    [1, 2, 3, 4, 5],
    [True, False, True],
    [sys.maxsize],
    [True, 10]
]

test_case_value_int = [
    [1.1, 1],
    ['test', 'c'],
    ['t', 'a', 'v', 'r', 'z'],
    [1.1, 1],
    [float('inf')],
    [float('-inf')],
    [None],
    [1, 'a', None, True],
    ['asd', True]
]
