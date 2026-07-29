class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        ans = []
        lex = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minlen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return ""
            for j in range(minlen):
                if w1[j] != w2[j]:
                    lex[w1[j]].add(w2[j])
                    break

        visited = {}

        def dfs(c):
            if c in visited:
                return visited[c]
            visited[c] = True
            for nxt in lex[c]:
                if dfs(nxt):
                    return True

            visited[c] = False
            ans.append(c)

        for c in lex:
            if dfs(c):
                return ""

        ans.reverse()
        return "".join(ans)
