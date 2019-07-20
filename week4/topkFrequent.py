from heapq import heappush, nlargest
from collections import Counter


class FrequentElem:
    def topKFrequent(self, nums, k):
        c = Counter(nums)
        t = [(count, i) for i, count in c.items()]
        h = []
        for p in t:
            heappush(h, p)

        return [i[0] for i in nlargest(k, h)]


print(FrequentElem().topKFrequent([1, 1, 1, 2, 2, 3], 2))
