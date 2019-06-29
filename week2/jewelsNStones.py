# Finds 'jewels' (characters) in 'stones' (string of chars) and returns total amount of jewels

from collections import defaultdict


class JewelsStones:
    def numJewelsInStones(self, J, S):
        jewelCount = {c: 0 for c in J}

        for c in S:
            if c in jewelCount:
                jewelCount[c] += 1

        return sum(jewelCount.values())


print(JewelsStones().numJewelsInStones('aA', 'aAAbbbb'))
