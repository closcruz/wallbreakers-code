from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def networkDelayTime(self, times, n, k):
        visited = set()
        dist = {i: float('inf') for i in range(1, n+1)}
        dist[k] = 0
        minDist = [(0, k)]
        g = defaultdict(list)

        for t in times:
            source, end, w = t[0], t[1], t[2]
            g[source].append((end, w))

        while minDist:
            curDist, curNode = heappop(minDist)
            if curNode in visited:
                continue
            visited.add(curNode)

            for n in g[curNode]:
                nextNode, nextDist = n[0], n[1]
                if nextNode in visited:
                    continue

                newDist = curDist + nextDist
                if newDist < dist[nextNode]:
                    dist[nextNode] = newDist
                    heappush(minDist, (newDist, nextNode))

        return -1 if len(visited) != len(dist) else dist[max(dist, key=dist.get)]


t1 = Solution()
print(t1.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
