# Given a no-empty array of ints, return the element that only appears once


class SingleNumber:
    def singleNumber(self, nums):
        numCount = {}

        for i in range(len(nums)):
            if nums[i] not in numCount:
                numCount[nums[i]] = 1
            else:
                numCount[nums[i]] += 1

        for x, y in numCount.items():
            if y == 1:
                return x
            else:
                continue


print(SingleNumber().singleNumber([4, 1, 2, 1, 2]))
