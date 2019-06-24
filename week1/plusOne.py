# Given an array represantation of a non negative integer, return that plus one


class PlusOne:
    def plusOne(self, digits):
        # digits = [str(x) for x in digits]
        # toInt = ''.join(digits)
        # rep = int(toInt)
        # out = str(rep + 1)
        # return [int(y) for y in out]
        return [int(y) for y in str(int(''.join([str(x) for x in digits])) + 1)]


print(PlusOne().plusOne([9]))
