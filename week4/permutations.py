class Permutation:
    def permutations(self, nums, start):
        if start == len(nums) - 1:
            yield nums
            return

        for _ in self.permutations(nums, start + 1):
            yield nums
            # Move from start to the right
            for i in range(start, len(nums) - 1):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                yield nums
            # Then move back to where we started from
            for i in range(len(nums) - 1, start, -1):
                nums[i], nums[i - 1] = nums[i - 1], nums[i]


for p in Permutation().permutations([1, 2, 3], 0):
    print(p[1])
