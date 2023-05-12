class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y



class Line:
    def __init__(self, p1, p2):
        self.a = p2.y - p1.y
        self.b = p1.x - p2.x
        self.c = p1.y * p2.x - p2.y * p1.x

    def contains_point(self, point):
        return self.a * point.x + self.b * point.y + self.c == 0


def test(canon, result):
    canon = sorted(canon)
    result = sorted(result)
    len_arr = len(canon)

    tmp = [Point(canon[i], result[i]) for i in range(len_arr)]
    forward_points = [tmp[0]]
    for i in range(1, len_arr):
        if tmp[i] != tmp[i - 1]:
            forward_points.append(tmp[i])

    tmp = [Point(canon[i], result[len_arr - 1 - i]) for i in range(len_arr)]
    backward_points = [tmp[0]]
    for i in range(1, len_arr):
        if tmp[i] != tmp[i - 1]:
            backward_points.append(tmp[i])

    len_forward = len(forward_points)
    len_backward = len(backward_points)

    if len_forward < 3 or len_backward < 3:
        return 'YES'

    line_forward = Line(forward_points[0], forward_points[1])
    line_backward = Line(backward_points[0], backward_points[1])
    forward = True
    backward = True
    for i in range(2, len_forward):
        if forward and not line_forward.contains_point(forward_points[i]):
            forward = False

    for i in range(2, len_backward):
        if backward and not line_backward.contains_point(backward_points[i]):
            backward = False
    if forward or backward:
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        len_canon = int(input())
        canon = input().split(' ')
        len_result = int(input())
        result = input().split(' ')

        if len_canon != len_result or len(set(canon)) != len(set(result)):
            print('NO')
        elif len_canon == 0:
            print('YES')
        else:
            canon = [int(i) for i in canon]
            result = [int(i) for i in result]
            print(test(canon, result))
