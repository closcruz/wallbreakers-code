class EditWord:
    # DP Method
    # def minDistance(self, word1, word2):
    #     l1, l2 = len(word1), len(word2)

    #     table = [[0 for j in range(l2+1)] for i in range(l1+1)]
    #     table[0] = [j for j in range(l2+1)]
    #     for i in range(l1+1):
    #         table[i][0] = i

    #     for i in range(1, l1+1):
    #         for j in range(1, l2+1):
    #             if word1[i-1] == word2[j-1]:
    #                 table[i][j] = table[i-1][j-1]
    #             else:
    #                 table[i][j] = 1 + \
    #                     min(table[i-1][j], table[i][j-1], table[i-1][j-1])

    #     return table[-1][-1]

    # Revursive with memoization
    def minDist(self, word1, word2):
        l1, l2 = len(word1), len(word2)

        memo = {}

        def dist(i, j):
            if i >= l1:  # Reached max index of word 1, rest of changes include dealing with the rest of word2
                return l2 - j
            if j >= l2:  # Same as above, just with word 2
                return l1 - i

            if (i, j) in memo:  # If we have number of changes so far for this position, return it
                return memo[(i, j)]
            elif word1[i] == word2[j]:
                memo[(i, j)] = dist(i+1, j+1)
                return memo[(i, j)]
            else:
                memo[(i, j)] = 1 + min(dist(i+1, j),
                                       dist(i, j+1), dist(i+1, j+1))
                return memo[(i, j)]

        return dist(0, 0)


print(EditWord().minDist('cor', 'ros'))
