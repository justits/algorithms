k = int(input())
a = [int(i) for i in input().split(' ')]
b = [int(i) for i in input().split(' ')]

all_sum = sum(a)
min_sum = sum(b)

box_num = all_sum if min_sum == 0 else min([a[i] // b[i] for i in range(k) if b[i] > 0])

while all_sum % box_num > 0:
    box_num -= 1
in_one_box = all_sum // box_num

c = [a[i] - b[i] * box_num for i in range(k)]

print(box_num, in_one_box)
i = 0

stat = ' '.join([' '.join([str(i+1)] * b[i]) for i in range(k)])
for _ in range(box_num):
    s = in_one_box - min_sum
    add = []
    while s > 0:
        while c[i] == 0:
            i += 1
        index = min(s, c[i])
        add += [str(i+1)] * index
        c[i] -= index
        s -= index
    if min_sum > 0:
        print(stat, ' '.join(add))
    else:
        print(' '.join(add))

