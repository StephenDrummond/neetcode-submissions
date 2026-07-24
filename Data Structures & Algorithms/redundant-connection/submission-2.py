class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        neighbors = {i:[] for i in range(len(edges) + 1)}
        for e, v in edges:
            neighbors[e].append(v)
            neighbors[v].append(e)
        cycle = set()
        visited = set()
        cyclestart = -1

        def dfs(node, prev):
            nonlocal cyclestart
            if node in visited:
                cyclestart = node
                return True
            
            visited.add(node)
            
            for nei in neighbors[node]:
                if nei == prev:
                    continue
                if dfs(nei, node):
                    if cyclestart != -1:
                        cycle.add(node)
                    if node == cyclestart:
                        cyclestart = -1
                    return True
            return False
        dfs(1, -1)
        for e, v in reversed(edges):
            if e in cycle and v in cycle:
                return [e, v]
        return []