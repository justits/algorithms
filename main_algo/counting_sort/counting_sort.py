def counting_sort(a):
    size_a = len(a)
    if size_a == 0:
        return a

    if not all(isinstance(x, (int, bool)) for x in a):
        raise TypeError("Sorting only integers or boolean")

    min_elem = min(a)
    max_elem = max(a)
    size_cnt = max_elem - min_elem + 1
    cnt = [0] * size_cnt
    for i in range(size_a):
        cnt[a[i] - min_elem] += 1

    i = 0
    for j in range(size_cnt):
        while cnt[j] > 0:
            a[i] = j + min_elem
            i += 1
            cnt[j] -= 1

    return a
