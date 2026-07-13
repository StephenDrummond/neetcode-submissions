class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        m1, m2 = height[0], height[-1]
        pre = [m1]
        suf = deque([m2])
        total = 0
        
        for i in range(1, n):
            m1 = max(height[i], m1)
            m2 = max(height[-i-1], m2)
            pre.append(m1)
            suf.appendleft(m2)
            
        for i in range(n):
            total += min(pre[i], suf[i]) - height[i]

        return total