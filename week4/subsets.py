class Subset:
    def subsets(self, A):
        n = len(A)
        out = []
        for k in range(1 << n):
            out.append([A[i] for i in range(n) if k & 1 << i])

        return out


t = Subset().subsets([1, 2, 3])
print(t)
