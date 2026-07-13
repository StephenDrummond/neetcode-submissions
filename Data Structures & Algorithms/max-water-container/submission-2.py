class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        most = 0

        while l < r:
            most = max(min(heights[r], heights[l]) * (r - l), most)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
            
        return most
