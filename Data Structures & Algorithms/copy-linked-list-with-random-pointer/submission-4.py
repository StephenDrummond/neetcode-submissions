class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        nodes = {}
        cur = head
        while cur:
            nodes[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            nodes[cur].next = nodes[cur.next] if cur.next else None
            nodes[cur].random = nodes[cur.random] if cur.random else None
            cur = cur.next

        return nodes[head]