class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ends = [2, 5, 8]
        colseen = [set() for _ in range(9)]
        blockseen = [[set() for _ in range(9)] for _ in range(9)]

        for i in range(9):
            row = board[i]
            rowseen = set()
            for j in range(9):
                x = row[j]
                if x in rowseen or x in colseen[j] or x in blockseen[i//3][j//3]:
                    return False
                elif x != '.':
                    colseen[j].add(x)
                    rowseen.add(x)
                    blockseen[i//3][j//3].add(x)

        return True