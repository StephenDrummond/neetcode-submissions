class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(word):
            l, r = 0, len(word)-1
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True
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