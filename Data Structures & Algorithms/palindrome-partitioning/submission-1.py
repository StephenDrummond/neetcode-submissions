class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(word):
            return word == word[::-1
            ]
        res = []
        cur = []

        def dfs(idx):
            if idx == len(s):
                res.append(cur[:])
                return
            for i in range(idx, len(s)):
                if isPalindrome(s[idx:i+1]):
                    cur.append(s[idx:i+1])
                    dfs(i+1)
                    cur.pop()
        
        dfs(0)
        return res