class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ans = []

        def dfs(cur, idx):
            s = sum(cur)
            if s == target:
                self.ans.append(cur)
            elif s > target: 
                return
            
            for i in range(idx, len(nums)):
                n = nums[i]
                cur.append(n)
                dfs(cur[:], i)
                cur.pop()
        
        dfs([], 0)
        return self.ans