# Returns the number of groups of special equivalent strings from a list of strings
# Two strings S and T are special-equivalent if after any number of moves, S == T


class SpecialEquivalent:
    def numSpecialEquivalent(self, A):
        return len(set(zip([''.join(sorted(w[::2])) for w in A], [''.join(sorted(w[1::2])) for w in A])))


print(SpecialEquivalent().numSpecialEquivalent(["a", "b", "c", "a", "c", "c"]))
