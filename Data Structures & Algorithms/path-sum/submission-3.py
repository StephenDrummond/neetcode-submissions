# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(cur, curval):
            if cur is None:
                return False
            if curval == targetSum and not cur.left and not cur.right:
                return True
            
            if (cur.left and dfs(cur.left, curval + cur.left.val)) or (cur.right and dfs(cur.right, curval + cur.right.val)):
                return True
            return False
            
        return dfs(root, root.val)

            