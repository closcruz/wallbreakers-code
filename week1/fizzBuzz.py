# Prints string representation of integers while replacing multiples of threes, fives and both with "Fizz", "Buzz", or "FizzBuzz" respectively


class FizzBuzz:
    def checkFizzBuzz(self, n):
        if (n % 3 == 0 and n % 5 == 0):
            return "FizzBuzz"
        elif (n % 5 == 0):
            return "Buzz"
        elif (n % 3 == 0):
            return "Fizz"
        else:
            return str(n)

    def fizzBuzz(self, n):
        arrToString = [x for x in range(1, n + 1)]
        out = map(self.checkFizzBuzz, arrToString)
        return list(out)
