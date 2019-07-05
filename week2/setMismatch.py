# Given a list representing a set, return duplicate number and the number it replaced

from collections import Counter


class SetMismatch:
    def findError(self, nums):
        check = Counter(nums)

        out = [0, 0]

        for i in range(len(nums)):
            if check.get(i+1, 0) == 0:
                out[1] = i+1

            if check.get(i+1) == 2:
                out[0] = i+1

        return out


print(SetMismatch().findError([1, 2, 2, 4]))
