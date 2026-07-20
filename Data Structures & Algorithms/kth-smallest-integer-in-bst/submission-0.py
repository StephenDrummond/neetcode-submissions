# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.stack = deque()

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            self.stack.append(node.val)
            dfs(node.right)
            
        
        dfs(root)
        val = 0
        for i in range(k):
            val = self.stack.popleft()
        return val
