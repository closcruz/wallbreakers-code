# Gets two indices and the values associated with them that sum up to the target

# This initial solution fails to use hasmaps, which make the compromis of using a bit more data for faster time complexity


class TwoSum:
    def twoSum(self, nums, target):
        out = []
        pos = [n for n in range(len(nums))]
        out.append(pos.pop())

        while(len(out) < 2):
            for i in pos:
                if (nums[out[0]] + nums[i] == target):
                    out.insert(0, i)
                    return out
            else:
                out[0] = pos.pop()


t1 = TwoSum().twoSum([2, 7, 5, 10], 9)
print(t1)
