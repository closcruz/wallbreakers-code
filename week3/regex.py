class Regex:
    # DP Method
    # def isMatch(self, s, p):
    #     table = [[False for c in range(len(p) + 1)] for r in range(len(s) + 1)]
    #     table[0][0] = True

    #     for i in range(1, len(table[0])):
    #         if p[i-1] == '*':
    #             table[0][i] = table[0][i-2]

    #     for i in range(1, len(table)):
    #         for j in range(1, len(table[0])):
    #             if s[i-1] == p[j-1] or p[j-1] == '.':
    #                 table[i][j] = table[i-1][j-1]
    #             elif p[j-1] == '*':
    #                 table[i][j] = table[i][j-2]
    #                 if p[j-2] == '.' or s[i-1] == p[j-2]:
    #                     table[i][j] = table[i][j] if table[i][j] else table[i-1][j]
    #             else:
    #                 table[i][j] = False

    #     return table[-1][-1]

    # Recursive method
    def isMatch(self, s, p):
        memo = {}

        def match(i, j):
            if not j:
                return i == ''

            if (i, j) in memo:
                return memo[(i, j)]

            res = False
            if len(j) > 1 and p[1] == '*':
                res = match(i, j[2:]) or (i != '' and (
                    i[0] == j[0] or j[0] == '.') and match(i[1:], j))
            else:
                res = i != '' and (j[0] == '.' or i[0] ==
                                   j[0]) and match(i[1:], j[1:])

            memo[(i, j)] = res
            return res

        return match(s, p)


print(Regex().isMatch("mississippi",
                      "mis*is*ip*."))
