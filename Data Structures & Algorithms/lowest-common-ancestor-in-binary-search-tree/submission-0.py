# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root
        if p.val > q.val: # keep p < q
            p, q = q, p
        
        while True:
            if p.val <= cur.val and q.val >= cur.val:
                return cur
            elif p.val <= cur.val and q.val <= cur.val:
                cur = cur.left
            elif p.val >= cur.val and q.val >= q.val:
                cur = cur.right
            else: break

        return cur