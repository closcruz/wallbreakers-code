# Checks if a string is isomorphic:
# Two strings are isomorphic if the characters in s can be replaced to get t.


class IsomorphicStr:
    def isIsomorpic(self, s, t):
        if len(set(s)) != len(set(t)):
            return False

        charMap = {}
        for i in range(len(s)):
            if s[i] in charMap:
                continue
            charMap[s[i]] = t[i]

        return "".join([charMap[c] for c in s]) == t


print(IsomorphicStr().isIsomorpic("abba", "abab"))
