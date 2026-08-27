class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        pre = [0] * len(boxes)
        suf = [0] * len(boxes)
        ans = [0] * len(boxes)

        count = 0
        for i in range(len(boxes)):
            if i > 0:
                pre[i] = pre[i-1] + count
            if int(boxes[i]) == 1:
                count += 1
        
        count = 0
        for i in range(len(boxes)-1, -1, -1):
            if i < len(boxes) - 1:
                suf[i] = suf[i+1] + count
            if int(boxes[i]) == 1:
                count += 1

        for i in range(len(boxes)):
            ans[i] = pre[i] + suf[i]
        return ans