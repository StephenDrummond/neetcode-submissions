class Letter:
    def __init__(self):
        self.branches = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Letter()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.branches:
                cur.branches[c] = Letter()
            cur = cur.branches[c]
        cur.end = True

    def search(self, word: str, start=None) -> bool:
        cur = start
        if not cur:
            cur = self.root
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                found = False
                for key, value in cur.branches.items():
                    found = self.search(word[i+1:], value) or found
                return found
            else: 
                if c not in cur.branches:
                    return False
            cur = cur.branches[c]
        return cur.end
