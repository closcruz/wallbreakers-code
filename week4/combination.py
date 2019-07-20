class Combination:
    def combos(self, n, k):
        if k == 0:
            return [[]]
        if len(n) == k:
            return [list(n)]

        out = [[n[0]] + i for i in self.combos(n[1:], k-1)]
        out += self.combos(n[1:], k)
        return out

    # Iterative solutions
    def combo(self, n, k):
        if k == 0 or k > n:
            return []
        if n == 1:
            return n

        # We get combo from first element up to n[i - 1]
        combo = [[i] for i in range(1, n-k+2)]
        for x in range(1, k):  # How many more elements we need to get a full combo
            combo = [c + [j]
                     for c in combo for j in range(c[-1] + 1, n-k+x+2)]


print(Combination().combos(range(1, 4+1), 2))
