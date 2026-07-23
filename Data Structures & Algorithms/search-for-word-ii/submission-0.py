class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

    def insert(self, word: str, i):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end= True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for i in range(len(words)):
            root.insert(words[i], i)
        
        res, seen = set(), set()
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, node, word):
            if (r < 0 or r >= ROWS 
                or c < 0 or c >= COLS 
                or (r, c) in seen or board[r][c] not in node.children):
                return

            seen.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.end:
                res.add(word)

            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            seen.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, '')
        return list(res)