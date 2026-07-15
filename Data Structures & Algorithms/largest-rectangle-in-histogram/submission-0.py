class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = heights[0]

        for i in range(len(heights)):
            j = i
            h = heights[i]
            while stack and h < stack[-1][0]:
                height, idx = stack.pop()
                j = idx
                ans = max(ans, height * (i - idx))
            stack.append((h, j))
        
        for h, i in stack:
            ans = max(ans, h * (len(heights) - i))

        return ans
