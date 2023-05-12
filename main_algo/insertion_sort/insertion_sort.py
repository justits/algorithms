def insertion_sort(a):
    size_a = len(a)
    for i in range(size_a):
        j = i
        while j > 0 and a[j - 1] > a[j]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1
    return a
