class Solution:
    def comboSum(self, candidates, target):
        def search(n, t, prev, res):
            for i in range(len(n)):
                if n[i] > t:
                    return

                if n[i] == t:
                    temp = [n[i]] + prev
                    temp.sort()
                    if temp not in res:
                        res.append(temp)

                    return
                else:
                    search(n[i:], t - n[i], prev + [n[i]], res)

        prev = []
        res = []
        candidates.sort()
        search(candidates, target, prev, res)
        return res


print(Solution().comboSum([3, 2, 6, 7], 7))
