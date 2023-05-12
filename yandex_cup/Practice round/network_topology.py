from time import time


def E():
    """
    Распределённая сеть состоит из n вычислительных узлов, соединённых с помощью
    помощью n−1 кабелей. Расстоянием между двумя узлами назовем минимальное
    количество соединений на цепочке от одного узла к другому.
    После выбора узлов-хранилищ, для каждого узла сети определяется
    ближайшее к нему хранилище. Ненадёжностью сети он называет максимальное
    значение этой величины по всем узлам.
    Какие узлы выбрать, чтобы ненадёжность сети была минимальна?
    Сатус: проходит часть тестов, не проходит по времени
    """
    from collections import defaultdict

    def longest_branch(graph, start, visited=None):
        t = time()
        if visited is None:
            visited = set()
        queue = [(start, 1), ]
        branch = []
        res = []
        while queue:
            root, lvl = queue.pop()
            queue.extend((n, lvl + 1) for n in graph[root] if n not in visited)

            if len(branch) >= lvl:
                if len(branch) > len(res):
                    res = branch.copy()
                while len(branch) >= lvl:
                    visited.remove(branch.pop())

            branch.append(root)
            visited.add(root)

        print(time() - t)
        if len(branch) > len(res):
            return branch
        else:
            return res

    # with open('input.txt', 'r') as f_in, open('output.txt', 'w') as f_out:
    n = int(input())
    if n <= 3:
        print('1 2')
        return

    net = defaultdict(list)  # для каждого узла множество смежных
    # связный граф с n узлами и n-1 ребрами - дерево
    for _ in range(n - 1):
        a, b = input().split()
        net[a].append(b), net[b].append(a)
    # у дерева всегда есть самый длинный путь, который можно найти используя два обхода
    longest_path = longest_branch(net, start='1')
    longest_path = longest_branch(net, start=longest_path[-1])
    # если бы требовалось найти один такой узел, то нужно было брать центр самого длинного пути
    # с двумя узлами: проделеаем это дважды
    n = len(longest_path) - 1
    split = n // 2
    # левая часть и центр
    lp = longest_branch(net, start=longest_path[0], visited={longest_path[n - split + 1], })
    split_left = lp[(len(lp) - 1) // 2]
    # правая часть и центр
    lp = longest_branch(net, start=longest_path[-1], visited={longest_path[split - 1], })
    split_right = lp[(len(lp) - 1) // 2]
    if split_left == split_right:
        # в случае симмитричного графа у нас может выбраться центральный узел дважды
        split_right = lp[(len(lp) - 1) // 2 + 1]

    print(f'{split_left} {split_right}')


if __name__ == '__main__':
    E()
