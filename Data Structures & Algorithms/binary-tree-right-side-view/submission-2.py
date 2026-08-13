# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([(root, 0)])
        postord = []

        if not root: return postord

        while q:
            cur, lvl = q.popleft()

            if lvl >= len(postord):
                postord.append([])
            postord[lvl].append(cur.val)

            if cur.left:
                q.append((cur.left, lvl + 1))
            if cur.right:
                q.append((cur.right, lvl + 1))

        
        return [x[-1] for x in postord]


