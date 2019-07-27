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
        return False

    def canFinish(self, num, prereqs):
        self.g = {}

        for pre in prereqs:
            c, p = pre[0], pre[1]
            if p not in self.g:
                self.g[p] = []

            self.g[p].append(c)

        self.visited = [False] * num
        self.inStack = [False] * num

        for i in range(num):
            if not self.visited[i] and self.cycle(i):
                return False

        return True


t1 = Solution()
print(t1.canFinish(2, [[0, 1], [1, 0]]))
