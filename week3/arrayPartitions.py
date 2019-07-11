class PairSum:
    def arrayPairSum(self, nums):
        nums.sort()
        out = []
        i = 0
        while i < len(nums):
            out.append(min(nums[i:i+2]))
            i += 2

        return sum(out)


print(PairSum().arrayPairSum([1, 4, 3, 2]))
