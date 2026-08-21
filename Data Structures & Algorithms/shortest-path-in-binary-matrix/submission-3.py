class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1: return -1
        q = deque([(1, 0, 0)])
        visited = set()
        direc = [[1, 0], [0, 1], [-1, 0], [0, -1], [-1, -1], [1, -1], [-1, 1], [1, 1]]
        

        while q:
            steps, curr, curc = q.popleft()
            print(curr, curc)
            if curr == n-1 and curc == n-1:
                return steps
            for dr, dc in direc:
                tr, tc = curr + dr, curc + dc
                if 0 <= tr < n and 0 <= tc < n and (tr, tc) not in visited and grid[tr][tc] == 0:
                    visited.add((tr, tc))
                    q.append((steps + 1, tr, tc))

        return -1
