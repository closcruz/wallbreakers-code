class ParenScore:
    def scoreOfParenthesis(self, S):
        sList = list(S)
        total = []

        while sList:
            total.append(sList.pop())

            if len(total) > 1:
                if total[-1] == '(' and total[-2] == ')':
                    total.insert(-2, 1)
                    del total[-1], total[-1]

                    if len(total) > 1:
                        if isinstance(total[-1], int) and isinstance(total[-2], int):
                            total.insert(-2, total[-1] + total[-2])
                            del total[-1], total[-1]
                elif len(total) >= 3:
                    if total[-1] == '(' and total[-3] == ')':
                        total.insert(-3, total[-2] * 2)
                        del total[-1], total[-1], total[-1]

                        if len(total) > 1:
                            if isinstance(total[-1], int) and isinstance(total[-2], int):
                                total.insert(-2, total[-1] + total[-2])
                                del total[-1], total[-1]

        return total[0]


print(ParenScore().scoreOfParenthesis("(())()"))
