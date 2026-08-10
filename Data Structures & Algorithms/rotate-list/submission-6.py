# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or head.next is None:
            return head
        cur, tail = head, head
        n = 0
        while cur:
            cur = cur.next
            n += 1
        k = k % n
        if k == 0:
            return head
        
        for i in range(n-k-1):
            head = head.next
        
        nxt = head.next
        head.next = None
        head = nxt

        cur = head
        while cur.next:
            cur = cur.next
        cur.next = tail

        return head