import math


def fly_swatter():
    f, R, t, r, g = [float(i) for i in input().split(' ')]
    r_interior = R - t - f
    g = g - 2 * f
    r = r + f

    if g <= 0:
        return 1
    num_lines = int((r_interior + r) // (2 * r + g)) * 2 + 2
    lines = [(2 * (i // 2) + 1) * r + (i + 1) // 2 * g for i in range(num_lines)]
    crossing = [math.sqrt(max(r_interior ** 2 - i ** 2, 0)) for i in lines]
    empty = 0.0
    for i in range(num_lines // 2):
        x = 2 * i
        for j in range(i, num_lines // 2):
            y = 2 * j
            if lines[x] ** 2 + lines[y] ** 2 <= r_interior ** 2:
                if lines[x + 1] ** 2 + (lines[y + 1]) ** 2 <= r_interior ** 2:
                    empty += g ** 2 * ((i != j) + 1)
                else:
                    if lines[y] < crossing[x + 1]:
                        if lines[x] <= crossing[y + 1]:
                            square = g ** 2 - (lines[x + 1] - crossing[y + 1]) * (lines[y + 1] - crossing[x + 1]) / 2
                            phi = math.asin(lines[y + 1] / r_interior) - math.acos(lines[x + 1] / r_interior)
                        else:
                            square = (crossing[x + 1] - lines[y]) * g + (crossing[x] - crossing[x + 1]) * g / 2
                            phi = math.acos(lines[x] / r_interior) - math.acos(lines[x + 1] / r_interior)
                    else:
                        if lines[x] < crossing[y + 1]:
                            square = (crossing[y + 1] - lines[x]) * g + (crossing[y] - crossing[y + 1]) * g / 2
                            phi = math.asin(lines[y + 1] / r_interior) - math.asin(lines[y] / r_interior)
                        else:
                            square = (crossing[y] - lines[x]) * (crossing[x] - lines[y]) / 2
                            phi = math.acos(lines[x] / r_interior) - math.asin(lines[y] / r_interior)
                    segment = r_interior ** 2 * (phi - math.sin(phi)) / 2
                    empty += (square + segment) * ((i != j) + 1)
    return 1 - empty * 4 / (math.pi * R ** 2)


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        result = fly_swatter()
        print('Case  #{}: {:.6f}'.format(t + 1, result))
