class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        cur = []
        def dfs(selection):
            if len(cur) == n:
                res.append(cur[:])
                return
            for i in range(len(selection)):
                cur.append(selection[i])
                dfs(selection[:i] + selection[i+1:])
                
                cur.pop()
            
        dfs(nums)
        return res
