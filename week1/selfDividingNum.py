# Check to see if number is self dividing and returns array of numbers that are
# Self Dividing = number is divisible by all its digits


class SelfDivideNum:
    def selfDivideCheck(self, n):
        digitsLeft = n
        while (digitsLeft != 0):
            check = digitsLeft % 10
            if (check == 0 or n % check != 0):
                return
            else:
                digitsLeft = digitsLeft // 10

        return n

    def selfDividingNumbers(self, left: int, right: int):
        numList = [x for x in range(left, right+1)]
        out = filter(lambda x: x != None, map(
            self.selfDivideCheck, numList))

        return list(out)
