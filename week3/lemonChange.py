class LemonadeChange:
    def lemonadeChange(self, bills):
        cust = [i for i in bills]
        register = {5: 0, 10: 0, 20: 0}

        if cust[0] != 5:
            return False

        correct = True
        while correct and len(cust) > 0:
            curr = cust.pop(0)

            if curr == 20:
                correct = correct and (
                    (register[5] > 0 and register[10] > 0) or register[5] > 2)
                register[20] += 1
                if register[10] == 0:
                    register[5] -= 3
                else:
                    register[5] -= 1
                    register[10] -= 1
            elif curr == 10:
                correct = correct and register[5] > 0
                register[10] += 1
                register[5] -= 1
            else:
                register[5] += 1

        return correct


print(LemonadeChange().lemonadeChange([5, 5, 5, 5, 10, 5, 10, 10, 10, 20]))
