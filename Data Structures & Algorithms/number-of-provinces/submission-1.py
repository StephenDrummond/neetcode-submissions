class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj = {i: set() for i in range(len(isConnected))}
        ROWS, COLS = len(isConnected), len(isConnected[0])
        ans = 0

        for r in range(ROWS):
            for c in range(COLS):
                if r == c:
                    continue
                if isConnected[r][c] == 1:
                    adj[r].add(c)
                    adj[c].add(r)

        visited = set()

                
        def bfs(idx):
            q = deque([idx])
            while q:
                cur = q.pop()
                for nei in adj[cur]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
                
        for i in range(ROWS):
            if i not in visited: 
                ans += 1
                bfs(i)
            else:
                continue

        

        return ans