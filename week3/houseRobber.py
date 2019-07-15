class HouseRobber:
    # Recursive method
    def robber(self, nums, isFirst, i):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2 or len(nums) == 3:
            return max(nums)
        elif i >= len(nums):
            return 0
        else:
            if i == 0:
                return max(nums[i] + self.robber(nums, True, i+2), self.robber(nums, False, i+1))
            if isFirst and i == len(nums) - 1:
                return 0
            else:
                return max(nums[i] + self.robber(nums, isFirst, i+2), self.robber(nums, isFirst, i+1))


print(HouseRobber().robber([1, 2, 3, 1], False, 0))
