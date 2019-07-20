class Baseball:
    def calcPoints(self, ops):
        ops.reverse()
        total = []

        while ops:
            op = ops.pop()
            try:
                total.append(int(op))
            except ValueError:
                if op == '+':
                    total.append(total[-1] + total[-2])
                elif op == 'D':
                    total.append(total[-1] * 2)
                else:
                    del total[-1]

        return sum(total)


print(Baseball().calcPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))
