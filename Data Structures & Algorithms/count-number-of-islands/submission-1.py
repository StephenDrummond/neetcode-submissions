class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        ans = 0
        seen = set()

        def bfs(r, c):
            q = deque()
            seen.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0,-1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r < ROWS and r >=0 and c < COLS 
                        and c >= 0 and grid[r][c] == '1' 
                        and (r, c) not in seen):
                        q.append((r, c))
                        seen.add((r, c))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in seen:
                    bfs(r, c)
                    ans += 1

        return ans


        
