# Checks to see if two strings are anagrams


class Anagram:
    def isAnagram(self, s, t):
        str1 = list(s)
        str2 = list(t)

        charMap = {}
        for i in str1:
            if (i in charMap):
                charMap[i] += 1
            else:
                charMap[i] = 1

        for j in str2:
            if (j in charMap):
                charMap[j] -= 1
            else:
                charMap[j] = 1

        charCount = list(charMap.values())
        isAnagram = True
        for n in charCount:
            isAnagram = isAnagram and not n

        return isAnagram


t1 = Anagram().isAnagram('carlos', 'cladfs')
print(t1)
