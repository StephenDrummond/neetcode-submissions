class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {x:[] for x in range(1,n+1)}
        for ui, vi, ti in times:
            adj[ui].append((vi, ti))
        
        dist = {x: math.inf for x in range(1, n+1)}
        q = deque([(k, 0)])
        dist[k] = 0

        while q:
            ui, dt = q.popleft()
            if dist[ui] < dt:
                continue
            for nei, t in adj[ui]:
                if dt + t < dist[nei]:
                    dist[nei] = dt + t
                    q.append((nei, dt + t))
        ans = max(dist.values())
        return ans if ans < math.inf else -1