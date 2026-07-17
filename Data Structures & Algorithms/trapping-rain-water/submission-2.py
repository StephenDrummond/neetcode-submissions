class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        pmx = 0
        smx = 0
        pre = [0] * len(height)
        suf = [0] * len(height)
        for i in range(len(height)):
            pmx = max(pmx, height[i])
            smx = max(smx, height[-i-1])
            pre[i] = pmx
            suf[-i-1] = smx
        
        for i in range(len(height)):
            h = height[i]
            ans += min(pre[i], suf[i]) - h

        return ans