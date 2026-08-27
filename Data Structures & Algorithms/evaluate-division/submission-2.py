class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        hm = defaultdict(dict)
        ans = []

        for vals, res in zip(equations, values):
            a, b = vals

            hm[a][b] = res
            hm[b][a] = 1/res

        for numer, denom in queries:
            visited = set()
            q = deque([(numer, 1)])
            ans.append(-1)

            while q:
                cur, val = q.pop()
                if denom in hm[cur]:
                    ans[-1] = val * hm[cur][denom]
                    break
                for nei in hm[cur]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, val * hm[cur][nei]))

        return ans