import bisect
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for i in range(len(tickets)):
            depart, dest = tickets[i]
            bisect.insort(adj[depart], (dest, i))
        ans = ["JFK"]
        n = len(tickets) + 1

        def dfs(cur, seen):
            print(cur, seen)
            if len(cur) == n:
                return cur
            for nei, idx in adj[cur[-1]]:
                if idx not in seen:
                    seen.add(idx)
                    cur.append(nei)
                    if dfs(cur, seen):
                        return cur
                    cur.pop()
                    seen.remove(idx)
            
        return dfs(["JFK"], set())