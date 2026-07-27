class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = {w:[] for w in wordList}
        seen = set()
        adj[beginWord] = []

        for i in range(len(wordList)):
            w = wordList[i]
            for j in range(len(beginWord)):
                if beginWord[:j] + beginWord[j+1:] == w[:j] + w[j + 1:]:
                    adj[beginWord].append(w)

        for i in range(len(wordList)):
            for j in range(len(wordList)):
                if i == j:
                    continue
                key, potential_val = wordList[i], wordList[j]
                for k in range(len(key)):
                    if key[:k] + key[k+1:] == potential_val[:k] + potential_val[k + 1:]:
                        adj[key].append(potential_val)
        q = deque([(beginWord, 1)])

        while q:
            cur, count = q.popleft()
            if cur == endWord:
                return count
            seen.add(cur)
            for val in adj[cur]:
                if val not in seen:
                    q.append((val, count + 1))
            

        return 0