class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = {(r, c): 0 for r in range(m) for c in range(n)}
        paths[(m-1, n-1)] = 1
        direc = [[-1, 0],[0, -1]] 
        q = deque([(m-1, n-1)])
        visited = set()

        while q:
            r, c = q.popleft()
            for dr, dc in direc:
                if r - dr < m and c - dc < n and r - dr >=0 and c - dc >= 0:
                    paths[(r, c)] += paths[(r-dr, c-dc)]

            for dr, dc in direc:
                if r + dr < m and c + dc < n and r + dr >= 0 and c + dc >= 0 and (r+dr, c+dc) not in visited:
                    visited.add((r+dr, c+dc))
                    q.append((r+dr, c + dc))
        return paths[(0,0)]




        