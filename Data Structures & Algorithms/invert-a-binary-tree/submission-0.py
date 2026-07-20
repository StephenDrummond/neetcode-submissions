# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        stack = deque([root])

        while stack:
            n = stack.popleft()
            n.left, n.right =  n.right, n.left

            if n.left:
                stack.append(n.left)
            if n.right:
                stack.append(n.right)
        return root