# Given two arrays return their intersection

from collections import defaultdict


class Intersection:
    def getIntersection(self, nums1, nums2):
        numCount1 = defaultdict(int)
        numCount2 = defaultdict(int)

        for i in nums1:
            numCount1[i] += 1

        for j in nums2:
            numCount2[j] += 1

        out = []
        for x in numCount1.keys():
            if x in numCount2:
                out.append(x)

        return out


print(Intersection().getIntersection([4, 9, 5], [9, 4, 9, 8, 4]))
