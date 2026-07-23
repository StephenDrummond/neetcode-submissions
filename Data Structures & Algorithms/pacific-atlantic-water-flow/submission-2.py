class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        r, c = ROWS // 2, COLS // 2
        q = deque([(r, c)])
        pac = [[False] * (COLS) for _ in range(ROWS)]
        atl = [[False] * (COLS) for _ in range(ROWS)]
        res = []

        pacific = []
        atlantic = []
        
        
        for i in range(ROWS):
            pac[i][0] = True
            pacific.append((i, 0))
            atl[i][COLS-1] = True
            atlantic.append((i, COLS-1))
        for i in range(COLS):
            pac[0][i] = True
            pacific.append((0, i))
            atl[ROWS-1][i] = True
            atlantic.append((ROWS-1, i))

        def bfs(source, directions, flowsinto):
            q = deque(source)
            seen = set()
            count = 0
            while q:
                r, c = q.popleft()
                
                count += 1
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if row < 0 or row >= ROWS or col < 0 or col >= COLS or (row,col) in seen:
                        continue
                    if flowsinto[r][c] and heights[r][c] <= heights[row][col]:
                        seen.add((row, col))
                        flowsinto[row][col] = True
                        q.append((row, col))

        bfs(atlantic, [[-1, 0], [0, -1],[0, 1], [1, 0]], atl)
        bfs(pacific, [[-1, 0], [0, -1],[0, 1], [1, 0]], pac)

        for r in heights:
            print(r)

        print()
        for r in atl:
            print(r)
        
        print()
        for r in pac:
            print(r)

        for r in range(ROWS):
            for c in range(COLS):
                if atl[r][c] and pac[r][c]:
                    res.append([r, c])

        return res