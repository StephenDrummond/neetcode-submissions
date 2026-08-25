"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return

        root = None
        nodes = defaultdict(Node)
        cur = head

        while cur:
            nodes[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        root = nodes[cur]
        ncur = root

        while cur:
            ncur = nodes[cur]
            ncur.next = nodes[cur.next] if cur.next else None
            ncur.random = nodes[cur.random] if cur.random else None

            cur = cur.next
            ncur = ncur.next

        return root