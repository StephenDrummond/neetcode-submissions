class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(oc, cc, cur):
            if oc == cc == 0:
                res.append(cur[:])
            if oc > 0:
                cur += '('
                dfs(oc-1, cc, cur)
                cur = cur[:-1]
            if cc > oc:
                cur += ')'
                dfs(oc, cc-1, cur)
                cur = cur[:-1]
        dfs(n, n, '')
        return res
            
