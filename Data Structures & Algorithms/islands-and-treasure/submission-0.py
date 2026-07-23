class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = (2**31) - 1
        ROWS, COLS = len(grid), len(grid[0])
        zeros = []
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    zeros.append((r, c, 0))
        q = deque(zeros)
        
        while q:
            r, c, val = q.popleft()
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or val > grid[r][c]:
                continue
            grid[r][c] = val
            directions = [[1,0],[-1,0],[0,1],[0,-1]]

            for dr, dc in directions:
                q.append((r + dr, c + dc, val + 1))

