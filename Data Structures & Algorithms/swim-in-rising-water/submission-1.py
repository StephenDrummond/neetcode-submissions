class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        mx = 0
        minheap = [(grid[0][0], 0,0)]

        while minheap:
            level, tx, ty = heapq.heappop(minheap)
            mx = max(mx, level)
            if tx == ROWS-1 and ty == COLS-1:
                break
            for dx, dy in directions:
                dx += tx
                dy += ty
                if dx < ROWS and dx >= 0 and dy < COLS and dy >= 0 and (dx, dy) not in visited:
                    visited.add((dx, dy))
                    heapq.heappush(minheap, (grid[dx][dy], dx, dy))


        return mx