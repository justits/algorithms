class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (other.x == self.x) and (other.y == self.y)

class Line:
    # a * x + b * y + c = 0
    def __init__(self, p1, p2):
        self.b = (p2.x - p1.x)
        self.a = (p1.y - p2.y)
        self.c = - self.b * p1.y - self.a * p1.x

    def intersect(self, other):
        y_intersect = (other.a * self.c - self.a * other.c) / (self.a * other.b - other.a * self.b)
        x_intersect = (other.c * self.b - self.c * other.b) / (self.a * other.b - other.a * self.b)
        return Point(x_intersect, y_intersect)

    def is_contain_point(self, point):
        return self.a * point.x + self.b * point.y + self.c == 0


def read_figure():
    params = [int(i) for i in input().split(' ')]
    if params[0] == 0:
        return Point(params[2], params[3])
    else:
        l1 = Line(Point(params[1], params[2]), Point(params[5], params[6]))
        l2 = Line(Point(params[3], params[4]), Point(params[7], params[8]))
        return l1.intersect(l2)


if __name__ == '__main__':
    n = int(input())
    ans = 'Yes'

    center1 = read_figure()
    center2 = center1
    i = 1
    while i < n and center2 == center1:
        center2 = read_figure()
        i += 1
    if center2 != center1:
        share_line = Line(center1, center2)
        for _ in range(n - i):
            new_center = read_figure()
            if ans == 'Yes':
                if not share_line.is_contain_point(new_center):
                    ans = 'No'
    print(ans)
