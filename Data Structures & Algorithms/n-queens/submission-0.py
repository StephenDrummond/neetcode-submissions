class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def diagonalclosed(x1: int, y1: int, cur: List[Set]) -> bool:
            for x2, y2 in cur:
                closed = (abs(x2-x1) == abs(y2-y1))
                if closed:
                    return True
            return False
        res = []
        rows = [x for x in range(n)]
        cols = [x for x in range(n)]
        
        def dfs(row, opencols, cur):
            if row == n:
                board = ['.' * c + 'Q' + '.' * (n-c-1) for _, c in sorted(cur)]
                res.append(board)
                return
            for i in range(len(opencols)):
                col = opencols[i]
                if diagonalclosed(row, col, cur):
                    continue
                cur.add((row, col))
                dfs(row+1, opencols[:i] + opencols[i+1:], cur)
                cur.remove((row, col))
        dfs(0, cols, set())
        return res