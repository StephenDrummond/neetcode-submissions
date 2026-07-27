class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = {w:[] for w in wordList + [beginWord]}
        alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
        
        for w in adj.keys():
            for i in range(len(w)):
                temp = w
                for l in alphabet:
                    if l == w[i]:
                        continue
                    temp = w[:i] + l + w[i+1:]
                    if temp in adj:
                        adj[w].append(temp)

        q = deque([(beginWord, 1)])
        seen = set()

        while q:
            cur, count = q.popleft()
            if cur == endWord:
                return count
            for w in adj[cur]:
                if w not in seen:
                    seen.add(cur)
                    q.append((w, count + 1))

        return 0