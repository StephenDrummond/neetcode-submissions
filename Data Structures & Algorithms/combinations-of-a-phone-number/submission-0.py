class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        rep = {'2':['a', 'b', 'c'],
        '3':['d', 'e', 'f'],
        '4':['g', 'h', 'i'],
        '5':['j', 'k', 'l'],
        '6':['m', 'n', 'o'],
        '7':['p', 'q', 'r', 's'],
        '8':['t', 'u', 'v'],
        '9':['w', 'x', 'y', 'z']}

        def dfs(idx, cur):
            print(cur)
            if idx == len(digits):
                if idx == 0:
                    return
                res.append(cur[:])
                return
            for c in rep[digits[idx]]:
                cur += c
                dfs(idx+1, cur)
                cur = cur[:-1]
        
        dfs(0, '')
        return res

