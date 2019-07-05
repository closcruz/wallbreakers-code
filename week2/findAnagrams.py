# Given strings s an p  find the start indices of p's anagrams in s

from collections import Counter


class FindAnagrams:
    def findAnagrams(self, s, p):
        pCheck = Counter(p)

        indices = []

        x, y = len(p), len(s)
        check = Counter(s[:x-1])
        for i in range(x - 1, y):
            check[s[i]] += 1

            if pCheck == check:
                indices.append(i - x + 1)

            check[s[i - x + 1]] -= 1
            if check[s[i - x + 1]] == 0:
                del check[s[i - x + 1]]

        return indices


print(FindAnagrams().findAnagrams("cbaebabacd", "abc"))
