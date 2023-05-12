import random


class Slice:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def len(self):
        return self.right - self.left


def quick_sort(a):
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

    def quick_sort_subarea(array_slice):
        if array_slice.len() > 1:
            pivot = a[random.randint(array_slice.left, array_slice.right - 1)]
            pivot_slice = split_by_pivot(array_slice, pivot)
            quick_sort_subarea(Slice(array_slice.left, pivot_slice.left))
            quick_sort_subarea(Slice(pivot_slice.right, array_slice.right))

    size_a = len(a)
    quick_sort_subarea(Slice(0, size_a))
    return a
