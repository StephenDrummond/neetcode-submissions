class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0
        stack = deque()
        ans = []

        while r < len(nums):
            if stack and nums[r] > stack[-1][0]:
                while stack and nums[r] > stack[-1][0]:
                    stack.pop()
            stack.append((nums[r], r))

            if stack[0][1] < l:
                stack.popleft()
            

            if r >= k - 1:
                ans.append(stack[0][0])
                l += 1

            r += 1
            

        return ans