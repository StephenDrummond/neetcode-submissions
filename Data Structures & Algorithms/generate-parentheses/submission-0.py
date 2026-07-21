class Solution:
    def isvalid(self, s:str) -> bool:
        q = []
        for c in s:
            if c == '(':
                q.append('(')
            if c == ')':
                if not q:
                    return False
                q.pop()
        return not q
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(oc, cc, cur):
            if len(cur) / 2 == n:
                if self.isvalid(cur):
                    res.append(cur[:])
            if oc > 0:
                cur += '('
                dfs(oc-1, cc, cur)
                cur = cur[:-1]
            if cc > 0:
                cur += ')'
                dfs(oc, cc-1, cur)
                cur = cur[:-1]
        dfs(n, n, '')
        return res
            
