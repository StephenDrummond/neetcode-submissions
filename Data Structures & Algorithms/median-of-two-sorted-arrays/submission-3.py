class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = (len(nums1) + len(nums2))
        half = total // 2
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        
        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2
            Aleft = A[i] if i >= 0 else -math.inf
            Aright = A[i+1] if i + 1 < len(A) else math.inf
            Bleft = B[j] if j >= 0 else -math.inf
            Bright = B[j+1] if j + 1 < len(B) else math.inf

            if Aleft <= Bright and Aright >= Bleft:
                if total % 2:
                    return min(Aright, Bright)
                else:
                    return (max(Bleft, Aleft) + min(Bright, Aright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
            
        