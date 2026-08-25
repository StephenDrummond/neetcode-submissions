class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        adj = {w:set() for w in wordList}

        for word in wordList:
            for i in range(len(word)):
                for word2 in wordList:
                    if word == word2: continue
                    if word[:i] + word[i+1:] == word2[:i] + word2[i+1:]:
                        adj[word].add(word2)
                        adj[word2].add(word)
        
        q = deque([(beginWord, 1)])
        visited = set()

        while q:
            w, steps = q.popleft()
            if w == endWord:
                return steps

            for nei in adj[w]:
                if nei not in visited:
                    visited.add(nei)
                    q.append((nei, steps + 1))

        return 0

                