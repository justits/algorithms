import random

from Slice import Slice


def k_order_statistic(a, k):
    def split_by_pivot(array_slice, pivot):
        pivot_slice = Slice()

        def find_left_pivot():
            left = array_slice.left
            for i in range(array_slice.left, array_slice.right):
                if a[i] < pivot:
                    a[left], a[i] = a[i], a[left]
                    left += 1
            return left

        def find_right_pivot():
            right = pivot_slice.left
            for i in range(pivot_slice.left, array_slice.right):
                if a[i] == pivot:
                    a[right], a[i] = a[i], a[right]
                    right += 1
            return right

        pivot_slice.left = find_left_pivot()
        pivot_slice.right = find_right_pivot()
        return pivot_slice

    def subarea_search(array_slice):
        if array_slice.len() == 1:
            return a[array_slice.left]
        pivot = a[random.randint(array_slice.left, array_slice.right - 1)]
        pivot_slice = split_by_pivot(array_slice, pivot)
        if k < pivot_slice.left:
            return subarea_search(Slice(array_slice.left, pivot_slice.left))
        elif k < pivot_slice.right:
            return a[pivot_slice.left]
        else:
            return subarea_search(Slice(pivot_slice.right, array_slice.right))

    size_a = len(a)
    if size_a <= k:
        raise TypeError("k can be less than array length")
    res = subarea_search(Slice(0, size_a))
    return res
