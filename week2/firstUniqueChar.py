# Returns index of the first unique character in a string, returns -1 if one does not exist

from collections import Counter


class UniqueChar:
    def findUniqueChar(self, s):
        charBag = Counter(s)
        nonRepeatChars = {k: v for k, v in charBag.items() if v == 1}

        if len(nonRepeatChars) == 0:
            return -1

        return s.find(list(nonRepeatChars.keys())[0])


print(UniqueChar().findUniqueChar('leetcode'))
