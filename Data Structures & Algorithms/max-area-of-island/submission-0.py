class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        ans = 0
        seen = set()

        def bfs(r, c):
            q = deque()
            area = 0
            q.append((r, c))
            directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]

            while q:
                row, col = q.popleft()
                area += 1
                

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r < ROWS and r >= 0 and c < COLS and c >= 0 
                        and grid[r][c] == 1 and (r, c) not in seen):
                        q.append((r, c))
                        seen.add((r, c))


            return area


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in seen:
                    seen.add((r, c))
                    ans = max(ans, bfs(r, c))

        return ans
