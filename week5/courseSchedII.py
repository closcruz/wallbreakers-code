class Solution:
    def cycle(self, node):
        self.visited[node] = True
        self.inStack[node] = True

        ne = self.g[node] if node in self.g else []
        for n in ne:
            if self.visited[n] == False:
                if self.cycle(n) == True:
                    return True
            elif self.inStack[n] == True:
                return True

        self.inStack[node] = False
        if node not in self.out:
            self.out.insert(0, node)
        return False

    def canFinish(self, num, prereqs):
        self.g = {}
        self.out = []

        for pre in prereqs:
            c, p = pre[0], pre[1]
            if p not in self.g:
                self.g[p] = []

            self.g[p].append(c)

        self.visited = [False] * num
        self.inStack = [False] * num

        for i in range(num):
            if not self.visited[i] and self.cycle(i):
                return []

        return self.out


t1 = Solution()
print(t1.canFinish(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
