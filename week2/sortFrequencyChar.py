# Given a string, sort and print out the characters in decreasing frequency

from collections import Counter


class LeastFrequent:
    def frequencySort(self, s):
        charBag = Counter(s)

        out = ""
        data = [(v, k) for k, v in charBag.items()]
        data.sort(reverse=True)
        for n, c in data:
            out += (c * n)

        return out


print(LeastFrequent().frequencySort("tree"))
