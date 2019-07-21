class Solution:
    def search(self, n, t):
        if not t:
            return True

        for i in range(len(n)):
            if i > 0 and n[i] == n[i-1]:
                continue

            if n[i] <= t and self.search(n[i+1:], t - n[i]):
                return True

        return False

    def canPartition(self, nums):
        s = sum(nums)
        if s % 2 == 1 or len(nums) < 2:
            return False
        nums.sort()
        return self.search(nums, s//2)


print(Solution().canPartition([1, 2, 3, 5]))
