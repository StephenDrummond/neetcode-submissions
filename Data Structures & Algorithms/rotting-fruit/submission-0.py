class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = []
        fruit = 0
        time = 0
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotten.append((r, c, 0))
                    fruit += 1
                elif grid[r][c] == 1:
                    fruit += 1
        
        q = deque(rotten)

        while q:
            r, c, t = q.popleft()
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0 or grid[r][c] == -1:
                continue
            fruit -= 1
            time = max(time, t)
            grid[r][c] = -1
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for dr, dc in directions:
                q.append((r + dr, c + dc, t + 1))
        
        return time if not fruit else -1