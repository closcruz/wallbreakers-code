# Checks a string and to see if it is a valid palindrome

import string


class Palindrome:
    def isPalindrome(self, s):
        cleanStr = [c for c in s.lower(
        ) if c not in string.punctuation and c != " "]

        left = 0
        right = len(cleanStr) - 1
        while left <= right:
            isPalindrome = True
            if isPalindrome:
                isPalindrome = cleanStr[left] == cleanStr[right]
                left += 1
                right -= 1
            else:
                break

        return isPalindrome


t1 = Palindrome().isPalindrome("race a car")
print(t1)
