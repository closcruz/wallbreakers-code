from collections import defaultdict


class Solution:
    def __init__(self):
        self.g = defaultdict(list)
        self.c = {}

    def addEdge(self, u, v):
        for i in v:
            self.g[u].append(i)

    def color(self, node):
        for n in self.g[node]:
            if n not in self.c:
                self.c[n] = 1-self.c[node]
                if not self.color(n):
                    return False
            else:
                if self.c[n] == self.c[node]:
                    return False

        return True

    def isBipartite(self):
        for i in range(len(self.g)):
            if i not in self.c:
                self.c[i] = 0
                if not self.color(i):
                    return False

        return True


t1 = Solution()
ex = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
for i, x in enumerate(ex):
    t1.addEdge(i, x)

print(t1.isBipartite())
