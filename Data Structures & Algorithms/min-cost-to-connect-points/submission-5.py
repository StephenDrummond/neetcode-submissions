class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
        def distance(x1, x2, y1, y2):
            return abs(x1-x2) + abs(y1-y2)

        adj = defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(len(points)):
                if i == j: continue
                x2, y2 = points[j]
                adj[(x1, y1)].append((distance(x1, x2, y1, y2), (x2, y2)))
        visited = set()
        minheap = [(0, next(iter(adj)))]
        p = 0
        c = 0
        n = len(adj)

        while minheap:
            dp, cur = heapq.heappop(minheap)
            
            if cur in visited:
                continue
            if c == n:
                break
            visited.add(cur)
            p += dp
            c += 1

            for np, node in adj[cur]:
                if node not in visited:
                    heapq.heappush(minheap, (np, node))

        return p