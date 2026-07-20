# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, mx):
            if node is None:
                return 0
            count = 0
            if node.val >= mx:
                count += 1
                mx = node.val
            return count + dfs(node.left, mx) + dfs(node.right, mx)
        return dfs(root, root.val)