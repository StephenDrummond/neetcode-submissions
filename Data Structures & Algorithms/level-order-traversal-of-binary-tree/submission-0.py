# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = deque([(root, 1)])
        if not root:
            return ans

        while q:
            n = q.popleft()
            if n[1] > len(ans):
                ans.append([])
            ans[n[1] - 1].append(n[0].val)
            if n[0].left:
                q.append((n[0].left, n[1] + 1))
            if n[0].right:
                q.append((n[0].right, n[1] + 1))

        return ans