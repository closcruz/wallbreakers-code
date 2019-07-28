class Solution:
    def getLenPath(self, r, c, n):
        if not 0 <= r < len(self.m) or not 0 <= c < len(self.m[0]) or self.m[r][c] <= n:
            return 0

        if self.lengths[r][c] != None:
            return self.lengths[r][c]

        currN = self.m[r][c]
        self.lengths[r][c] = max(self.getLenPath(r-1, c, currN), self.getLenPath(r+1, c, currN),
                                 self.getLenPath(r, c-1, currN), self.getLenPath(r, c+1, currN))+1

        return self.lengths[r][c]

    def longestIncPath(self, matrix):
        self.m = matrix
        self.lengths = [[None for j in range(
            len(matrix[0]))] for i in range(len(matrix))]

        out = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                out = max(out, self.getLenPath(r, c, -float('inf')))

        return out


t1 = Solution()
print(t1.longestIncPath([[9, 9, 4],
                         [6, 6, 8],
                         [2, 1, 1]]))
