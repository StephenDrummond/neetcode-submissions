class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []

        for i in range(len(nums)):
            while q and nums[i] > q[-1][0]:
                q.pop()
            
            q.append((nums[i], i))
            
            if q[0][1] <= i - k:
                q.popleft()

            if i >= k-1:
                ans.append(q[0][0])
                

        return ans