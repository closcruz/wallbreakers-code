#   Returns number of sets of seperate friends

from collections import defaultdict


class FriendCircle:
    def getRoot(self, parent, x):
        while parent[x] != x:
            x = parent[x]

        return x

    def friendCircleNum(self, M):
        # Used to track which element has which parent
        parent = [i for i in range(3)]

        # Since matrix is reflective along its diagnol and always a perfect square, last row wont be relevant and will be used to store data
        M[-1] = [1 for i in range(len(M))]

        for i in range(len(M)):
            # Again, since matrix is reflective, we only need to check one side of it's diagnol for data
            for j in range(i + 1, len(M)):
                # If value at [i][j] = 1 then student i is direct friends with j, so we will set with them
                if M[i][j]:
                    n1 = self.getRoot(parent, i)
                    n2 = self.getRoot(parent, j)
                    # If both have same parent, then both nodes are in same set (already friends) so we skip
                    if n1 == n2:
                        continue
                    # Else, make the set and tally the number of elements that a root has under it in the last row
                    M[-1][n1] += M[-1][n2]
                    parent[n2] = n1
                    M[-1][n2] = 0   # Denotes node has parent besides itself

        sets = 0
        for i in M[-1]:
            if i:
                sets += 1

        return sets


print(FriendCircle().friendCircleNum([[1, 1, 0],
                                      [1, 1, 0],
                                      [0, 0, 1]]))
