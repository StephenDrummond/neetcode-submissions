class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        adj = {x: [] for x in range(n)}
        for depart, dest, cost in flights:
            adj[depart].append((cost, dest))

        minheap = []
        visited = set()
        cost = 0
        heapq.heappush(minheap, (0,0,src))

        while minheap:
            cost, stops, cur = heapq.heappop(minheap)
            if cur in visited or stops > k+1:
                continue
            elif cur == dst:
                return cost
            
            for c, dest in adj[cur]:
                heapq.heappush(minheap, (cost + c, stops + 1, dest))


        return -1
