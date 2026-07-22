class Node:
    def __init__(self):
        self.branches = {}
        self.end = False

class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None: 
        cur = self.root
        for c in word:
            if c not in cur.branches:
                cur.branches[c] = Node()
            cur = cur.branches[c]
        cur.end = True


    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.branches:
                return False
            cur = cur.branches[c]
        return cur.end


    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.branches:
                return False
            cur = cur.branches[c]
        return True
        