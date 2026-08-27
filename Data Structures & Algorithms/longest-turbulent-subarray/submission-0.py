class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        mx = 1
        cur = 1
        increasing = 0 #even == 0, increasing == 1, decreasing == -1

        for i in range(len(arr)-1):
            print(increasing, arr[i], arr[i+1], cur)
            if arr[i+1] > arr[i]:
                cur += 1
                if increasing != -1:
                    cur = 2
                increasing = 1
            elif arr[i+1] < arr[i]:
                cur += 1
                if increasing != 1:
                    cur = 2
                increasing = -1
            else:
                increasing = 0
                cur = 1
            mx = max(mx, cur)

        return mx