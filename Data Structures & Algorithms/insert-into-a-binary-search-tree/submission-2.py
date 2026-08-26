# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        cur = root
        prev = None

        while cur:
            if val > cur.val:
                prev = cur
                cur = cur.right
            elif val < cur.val:
                prev = cur
                cur = cur.left
        
        if val < prev.val:
            prev.left = TreeNode(val)
        elif val > prev.val:
            prev.right = TreeNode(val)
        
        return root