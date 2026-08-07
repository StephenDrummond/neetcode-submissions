class Solution:
    def trap(self, height: List[int]) -> int:
        pre = []
        suf = []
        mp = 0
        ms = 0

        total = 0

        for i in range(len(height)):
            mp = max(mp, height[i])
            pre.append(mp)
            ms = max(ms, height[-1-i])
            suf.append(ms)

        for i in range(len(pre)):
            total += min(pre[i], suf[-1-i]) - height[i]

        return total