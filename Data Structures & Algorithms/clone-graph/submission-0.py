"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        q = deque([node])
        hm = {}
        hm[node] = Node(node.val)

        while q:
            cur = q.popleft()
            for n in cur.neighbors:
                if n not in hm:
                    hm[n] = Node(n.val)
                    q.append(n)
                hm[cur].neighbors.append(hm[n])
        return hm[node]
