# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy numbers.


class HappyNumber:
    def isHappy(self, n):
        nList = list(str(n))
        tries = []
        out = True
        check = True

        while check:
            total = sum([int(x) ** 2 for x in nList])
            nList = list(str(total))

            if total == 1:
                check = False
            elif total not in tries:
                tries.append(total)
            else:
                out = False
                check = False

        return out


print(HappyNumber().isHappy(19))
