class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        island1 = set()
        island2 = set()
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, island, other):
            if r >= ROWS or r < 0 or c >= COLS or c < 0 or (r, c) in island or (r, c) in other or grid[r][c] == 0:
                return
            
            island.add((r, c))
            for dr, dc in directions:
                dfs(dr + r, dc + c, island, other)


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    continue
                if not island1:
                    dfs(r, c, island1, island2)
                    continue
                dfs(r, c, island2, island1)

        q = deque([(x, 0) for x in island1])
        visited = set()
        while q:
            cur, bridges = q.popleft()
            print(cur, bridges)
            if cur in island2:
                return bridges -1
            for dr, dc in directions:
                r, c = cur[0] + dr, cur[1] + dc
                if r >= 0 and r < ROWS and c >= 0 and c < COLS and (r, c) not in island1 and (r, c) not in visited:
                    visited.add((r, c))
                    q.append(((r, c), bridges + 1))               


        return 0