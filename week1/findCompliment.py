# Find bitwise compliment of given integer


class FindCompliment:
    # ~ compliment uses twos compliments which takes into account leading 1 or 0 for negative numbers
    # This method uses string methods to implement ones compliment method by switching all 1 to 0 and 0 to 1
    # bin() returns a string of binary representation of a number, with first two spaces reserved for a leading 0 or 1 to represent negative nums
    def findCompliment(self, num):
        return int((bin(num)[2:].replace('0', '2').replace('1', '0').replace('2', '1')), 2)


t1 = FindCompliment().findCompliment(5)
print(t1)
