class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        ans = 0

        def explore(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == '0' or (r, c) in seen:
                return
            seen.add((r, c))
            
            explore(r+1, c)
            explore(r-1, c)
            explore(r, c+1)
            explore(r, c-1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in seen:
                    explore(r, c)
                    ans += 1

        return ans