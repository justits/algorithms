T = int(input())
for t in range(T):
    N, K = map(int, input().split(' '))
    start_room, passages = map(int, input().split(' '))
    ans = passages
    if K < N:
        not_visit = {i for i in range(1, N + 1) if i != start_room}
        add_ans = 0
        steps = K // 2
        for _ in range(steps):
            next_room = not_visit.pop()
            print('T', next_room)
            _, passages = map(int, input().split(' '))
            ans += passages

            print('W')
            next_room, passages = map(int, input().split(' '))
            if next_room in not_visit:
                add_ans += passages
                not_visit.remove(next_room)

        if K % 2 == 1:
            next_room = not_visit.pop()
            print('T', next_room)
            _, passages = map(int, input().split(' '))
            ans += passages
        ans = (ans / (steps + K % 2 + 1) * (N - steps) + add_ans)

    else:
        for i in range(1, N + 1):
            if i != start_room:
                print('T', i)
                _, passages = map(int, input().split(' '))
                ans += passages

    print('E', int(ans / 2))