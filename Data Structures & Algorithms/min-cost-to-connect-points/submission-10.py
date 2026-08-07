class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i:[] for i in range(N)}
        total = 0
        visited = set()
        heap = [(0, 0)]
        def dist (x1, y1, x2, y2):
            return abs(x1-x2) + abs(y1-y2)
        
        for i in range(N):
            x1, y1 = points[i]
            for j in range(N):
                if i == j:
                    continue
                x2, y2 = points[j]
                x = dist(x1, y1, x2, y2)
                adj[i].append((x, j))
                adj[j].append((x, i))
        
        while heap and len(visited) < N:
            cost, i = heapq.heappop(heap)
            if i in visited: continue

            total += cost
            visited.add(i)
            for neicost, j in adj[i]:
                if j not in visited:
                    heapq.heappush(heap, (neicost, j))

        return total