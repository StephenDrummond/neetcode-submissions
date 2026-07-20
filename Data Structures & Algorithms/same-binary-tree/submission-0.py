# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            print(q1, q2)
            n1 = q1.popleft()
            n2 = q2.popleft()

            if n1 and n2:
                if n1.val != n2.val:
                    return False
            elif n1 and not n2:
                return False
            elif not n1 and n2:
                return False
            else: continue

            q1 += [n1.left, n1.right]
            q2 += [n2.left, n2.right]
        return True
