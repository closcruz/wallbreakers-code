class Rotate:
    def rotateArray(self, nums, k):
        for _ in range(k):
            nums.insert(0, nums[-1])
            del nums[-1]


nums = [1, 2, 3, 4, 5, 6]
Rotate().rotateArray(nums, 3)
print(nums)
