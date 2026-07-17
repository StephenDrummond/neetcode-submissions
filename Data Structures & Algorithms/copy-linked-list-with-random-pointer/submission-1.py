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
        if head == None:
            return

        newhead = Node(head.val)
        cur = head
        newcur = newhead
        i = 0
        hm = defaultdict(list)
        nodes = []

        while cur:
            if cur.next:
                newcur.next = Node(cur.next.val)
            
            hm[cur.random].append(i)
            nodes.append(newcur)

            newcur = newcur.next
            cur = cur.next
            i += 1
        
        cur = head
        newcur = newhead

        while newcur:
            if cur in hm:
                for nd in hm[cur]:
                    nodes[nd].random = newcur
            
            newcur = newcur.next
            cur = cur.next
        return newhead