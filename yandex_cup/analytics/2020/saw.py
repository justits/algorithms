MAX_BORDER = int(10e12)
MIN_BORDER = int(-10e12)

def to_int(saw, idx):
    try:
        return int(saw[idx])
    except:
        return MAX_BORDER if idx % 2 else MIN_BORDER


def find_saw(n, saw, fill_values):
    fill_values.sort()

    # Find the missing indexes
    decrease_fill = [i + 1 for i in range(0, n, 2) if saw[i] == '-']
    increase_fill = [i + 1 for i in range(1, n, 2) if saw[i] == '-']

    saw = [to_int(saw[i], i) for i in range(n)]
    # Add borders for extreme values
    saw = [MAX_BORDER] + saw + ([MAX_BORDER] if n % 2 == 0 else [MIN_BORDER])

    # Check if it is possible to make a saw
    if sum([saw[i] > min(saw[i - 1], saw[i + 1]) for i in range(1, n + 1, 2)]):
        return False
    if sum([saw[i] < max(saw[i - 1], saw[i + 1]) for i in range(2, n + 1, 2)]):
        return False

    decrease_fill.sort(key=lambda x: min(saw[x - 1], saw[x + 1]))
    for i in decrease_fill:
        if fill_values[0] > min(saw[i - 1], saw[i + 1]):
            return False
        saw[i] = fill_values.pop(0)

    increase_fill.sort(key=lambda x: max(saw[x - 1], saw[x + 1]), reverse=True)
    for i in increase_fill:
        if fill_values[-1] < min(saw[i - 1], saw[i + 1]):
            return False
        saw[i] = fill_values.pop(-1)

    return saw[1:-1]


if __name__ == "__main__":
    n, k = map(int, input().split())
    a = [val if val != '-' else val for val in input().split()]
    fill_values = list(map(int, input().split()))
    ans = find_saw(n, a, fill_values)

    if ans:
        print(" ".join(map(str, ans)))
    else:
        print('NO SOLUTION')
