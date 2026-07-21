class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []

        def dfs(i):
            sm = sum(cur)
            if sm > target:
                return
            if sm == target:
                res.append(cur[:])
            
            for j in range(i,len(nums)):
                cur.append(nums[j])
                dfs(j)
                cur.pop()
            

        dfs(0)
        return res