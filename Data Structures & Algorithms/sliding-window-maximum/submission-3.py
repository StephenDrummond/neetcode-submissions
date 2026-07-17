class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = deque() #index, val
        ans = [0] * (len(nums) - k + 1)
        for i in range(len(nums)):
            x = nums[i]
            if stack and x > stack[-1][1]:
                while stack and x > stack[-1][1]:
                    stack.pop()
                stack.append((i, x))
            else: 
                stack.append((i, x))
            
            if stack and stack[0][0] < i - k + 1:
                stack.popleft()
            if i-k+1 >= 0:
                ans[i-k+1] = stack[0][1]
        

        return ans