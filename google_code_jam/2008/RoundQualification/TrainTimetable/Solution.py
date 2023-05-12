def find_trains(trip, empty):
    trip = sorted(trip)
    empty = sorted(empty)
    i = 0
    trains = 0
    for t in trip:
        if i < len(empty) and empty[i] <= t:
            i += 1
        else:
            trains += 1
    return trains


def to_min(h_m):
    h_m = h_m.split(':')
    return int(h_m[0]) * 60 + int(h_m[1])


def train_timetable():
    turnaround = int(input())
    na, nb = [int(i) for i in input().split(' ')]

    empty_b = [0] * na
    trip_a = [0] * na
    for i in range(na):
        trip_a[i], empty_b[i] = [to_min(i) for i in input().split(' ')]
        empty_b[i] += turnaround

    empty_a = [0] * nb
    trip_b = [0] * nb
    for i in range(nb):
        trip_b[i], empty_a[i] = [to_min(i) for i in input().split(' ')]
        empty_a[i] += turnaround

    return find_trains(trip_a, empty_a), find_trains(trip_b, empty_b)


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        start_a, start_b = train_timetable()
        print('Case  #{}: {} {}'.format(t + 1, start_a, start_b))

