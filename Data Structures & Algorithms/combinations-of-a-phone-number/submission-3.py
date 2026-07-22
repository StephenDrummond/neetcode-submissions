class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        res = []
        rep = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }


        def dfs(idx, cur):
            if idx == len(digits):
                res.append(cur)
                return
            for c in rep[digits[idx]]:
                dfs(idx+1, cur + c)
        
        dfs(0, '')
        return res

