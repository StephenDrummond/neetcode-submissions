class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        os = set()
        seen = set()

        def bfs(r, c):
            seen.add((r, c))
            q = deque([(r, c)])
            mem = []
            directions = [[-1, 0], [0, -1],[0, 1], [1, 0]]
            contained = True

            while q:
                r, c = q.popleft()
                
                if (r, c) in os:
                    contained = False
                if (r >= ROWS - 1 or r < 1 
                    or c >= COLS - 1 or c < 1 
                    or board[r][c] == 'X'):
                    continue
                mem.append((r, c))
                for dr, dc in directions:
                    if (r + dr, c + dc) not in seen:
                        q.append((r + dr, c + dc))
                        seen.add((r + dr, c + dc))
            if contained:
                for r, c in mem:
                    board[r][c] = 'X'

        for c in range(COLS):
            if board[0][c] == 'O':
                os.add((0,c))
            if board[ROWS-1][c] == 'O':
                os.add((ROWS-1, c))
        for r in range(ROWS):
            if board[r][0] == 'O':
                os.add((r,0))
            if board[r][COLS-1] == 'O':
                os.add((r, COLS-1))
        
        print(os)
        
        for r in range(1,ROWS-1):
            for c in range(1, COLS-1):
                if board[r][c] == 'O' and (r, c) not in seen:
                    bfs(r, c)
