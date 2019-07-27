class Solution:
    def search(self, r, c, i):
        if i == len(self.w):
            return True

        if not 0 <= r < len(self.b) or not 0 <= c < len(self.b[0]):
            return False

        if self.b[r][c] != self.w[i] or self.v[r][c] == True:
            return False

        else:
            self.v[r][c] = True
            out = self.search(r, c-1, i+1) or self.search(r, c+1, i +
                                                          1) or self.search(r-1, c, i+1) or self.search(r+1, c, i+1)

            self.v[r][c] = False
            return out

    def exist(self, board, word):
        self.b = board
        self.w = word
        self.v = [[False for j in range(len(board[0]))]
                  for i in range(len(board))]

        for r in range(len(self.b)):
            # Find column indices for starting letter of word in each row
            for c in [i for i, n in enumerate(self.b[r]) if n == word[0]]:
                if self.search(r, c, 0):
                    return True


t1 = Solution()
t1.exist([['A', 'B', 'C', 'E'],
          ['S', 'F', 'C', 'S'],
          ['A', 'D', 'E', 'E']], 'SEE')
