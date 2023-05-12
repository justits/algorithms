class Graph:
    class Node:
        def __init__(self):
            self.neighbords = []
            self.end = False
            self.check = False

    def __init__(self, n):
        self.n = n
        self.nodes = [self.Node() for _ in range(n)]
        self.nodes[-1].end = True
        self.m = 0

    def add_edge(self, u, v):
        self.nodes[u].neighbords.append(self.nodes[v])
        self.nodes[v].neighbords.append(self.nodes[u])

    def find_res(self):
        num = 1
        sum = 0
        self.nodes[0].check = True
        for node in self.nodes[0].neighbords:
            node.check = True
            end, sum_n, num_n = self.sub_res(node, 1)
            num += num_n
            sum += sum_n

        num -= 2
        ans = (self.m + 1) * (self.m // 2) + (self.m - self.m // 2) * (self.m % 2)
        ans *= num
        ans += self.m * sum
        ans += (self.m * ((self.m - 1) // 2) + (self.m - 1 - (self.m - 1) // 2) * ((self.m - 1) % 2)) * 2
        ans += self.m * (self.n * (self.n - 1) / 2 - self.m * num - (self.m - 1) * 2)
        return ans

    def sub_res(self, node, k):
        node.check = True
        end = node.end
        self.m = k if end else self.m
        k = 0 if end else k
        sum = k
        num = 1
        for n in node.neighbords:
            if not n.check:
                end_s, sum_s, num_s = self.sub_res(n, k + 1)
                if end_s:
                    end, sum, num = end_s, sum_s, num_s
                    break
                else:
                    sum += sum_s
                    num += num_s

        return [end, sum, num]



n = int(input())
g = Graph(n)
for _ in range(n - 1):
    u, v = [int(i) for i in input().split(' ')]
    g.add_edge(u - 1, v - 1)
print(int(g.find_res()))