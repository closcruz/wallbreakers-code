class Solution:        
    def partitionEqualSums(self, nums):
        if sum(nums) % 2 == 1:
            return False
        if len(nums) == 2:
            return nums[0] == nums[1]
        else:
            for i in range(len(nums)):
                val = [nums[i]]
                part = nums[:len(nums) - 1]
                for j in range(len(part)):
                    new_part = part[j] + val
                    if self.partitionEqualSums(new_part):
                        return True

            return False


print(Solution().partitionEqualSums([1,5,5,11]))
