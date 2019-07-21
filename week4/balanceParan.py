class Balance:
    def balanceParanthesis(self, n):
        if n == 0:
            return ['']
        if n == 1:
            return ['()']

        tbl = [['']]
        for t in range(1, n + 1):
            res = []
            for i in range(t):
                for x in tbl[i]:
                    for y in tbl[t - i - 1]:
                        res.append('(' + x + ')' + y)

            tbl.append(res)

        tbl[n].sort()
        return tbl[n]


print(Balance().balanceParanthesis(3))
