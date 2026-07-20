# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.mx = -math.inf
        def dfs(node):
            if not node:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)
            cur = 0
            if l > 0:
                cur += l
            if r > 0:              
                cur += r
            self.mx = max(self.mx, cur + node.val)
            
            return node.val + max(l, r, 0)
        dfs(root)
        return self.mx

