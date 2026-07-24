class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        neighbors = {i:[] for i in range(n)}
        for n1, n2 in edges:
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)

        def dfs(node, prev):
            visited.add(node)

            for nei in neighbors[node]:
                if nei == prev:
                    continue
                if nei in visited or not dfs(nei, node) or nei == node:
                    return False
            return True
       
        
        valid = dfs(0, -1)
        return len(visited) == n and valid