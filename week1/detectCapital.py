# Detects if usage of capital in string is correct using criteria:
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".

from functools import reduce

# Can be simplified removing map to check if each char is capital
# Also can jsut use string functions to get answer word.istitle or word.isupper or word.islower


class DetectCapital:
    def isCapital(self, c):
        return 65 <= ord(c) <= 90

    def detectCapital(self, word):
        isCapArr = list(map(self.isCapital, list(word)))

        return reduce(lambda x, y: x and y, isCapArr) or not reduce(lambda x, y: x or y, isCapArr) or (isCapArr[0] and reduce(lambda x, y: x and y, isCapArr[1:]))


t1 = DetectCapital().detectCapital('FlaG')
print(t1)
