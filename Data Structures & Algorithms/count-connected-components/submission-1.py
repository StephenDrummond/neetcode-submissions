class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ans = 0
        neighbors = {i:[] for i in range(n)}
        for e1, e2 in edges:
            neighbors[e1].append(e2)
            neighbors[e2].append(e1)
        visited = set()
        
        print(neighbors)

        def dfs(node, prev):
            visited.add(node)

            for nei in neighbors[node]:
                if nei == prev:
                    continue
                if nei not in visited:
                    dfs(nei, node)
        
        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                ans += 1

        return ans