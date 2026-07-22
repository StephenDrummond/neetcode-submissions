class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        cur = []
        word = list(word)
        rows = len(board)
        cols = len(board[0])
        seen = set()
        
        def dfs (seen, i, j, idx):
            if idx == len(word):
                return True
            if i+1 < rows and board[i+1][j] == word[idx] and (i+1, j) not in seen:
                seen.add((i+1, j))
                if dfs(seen, i+1, j, idx+1):
                    return True
                seen.remove((i+1, j))
            if i-1 >= 0 and board[i-1][j] == word[idx] and (i-1, j) not in seen:
                seen.add((i-1, j))
                if dfs(seen, i-1, j, idx+1):
                    return True
                seen.remove((i-1, j))
            if j+1 < cols and board[i][j+1] == word[idx] and (i, j+1) not in seen:
                seen.add((i, j+1))
                if dfs(seen, i, j+1, idx+1):
                    return True
                seen.remove((i, j+1))
            if j-1 >= 0 and board[i][j-1] == word[idx] and (i, j-1) not in seen:
                seen.add((i, j-1))
                if dfs(seen, i, j-1, idx+1):
                    return True
                seen.remove((i, j-1))
            return False


        for i in range(rows):
            row = board[i]
            for j in range(cols):
                cell = row[j]
                if cell == word[0]:
                    seen.add((i, j))
                    if dfs(seen, i, j, 1):
                        return True
                    seen.remove((i, j))
                    continue
                

        return False