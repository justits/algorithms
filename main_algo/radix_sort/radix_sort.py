def radix_sort(a, numeral_system=10):
    def get_rank(elem):
        return ((elem - min_elem) // exp) % numeral_system

    def counting_sort():
        cnt = [0] * numeral_system
        for i in range(size_a):
            rank = get_rank(a[i])
            cnt[rank] += 1

        start_range = [0] * numeral_system
        for i in range(1, numeral_system):
            start_range[i] = start_range[i - 1] + cnt[i - 1]

        sorted_a = [0] * size_a
        for i in range(size_a):
            rank = get_rank(a[i])
            sorted_a[start_range[rank]] = a[i]
            start_range[rank] += 1

        return sorted_a

    size_a = len(a)
    if size_a == 0:
        return a

    if not all(isinstance(x, (int, bool)) for x in a):
        raise TypeError("Sorting only integers or boolean")

    max_elem = max(a)
    min_elem = min(a)
    exp = 1
    while exp <= max_elem - min_elem:
        a = counting_sort()
        exp *= numeral_system

    return a
