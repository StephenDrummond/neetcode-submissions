# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        if head.next is None:
            return

        while fast and fast.next:
            last = slow
            slow = slow.next
            fast = fast.next.next
        last.next = None

        prev = None
        cur = slow
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        secondhead = prev
        cur = head
        last = cur
        while cur:
            nxt = cur.next
            secondnxt = secondhead.next
            cur.next = secondhead
            secondhead.next = nxt
            last = cur
            cur = nxt
            secondhead = secondnxt
        if secondhead:
            last.next.next = secondhead
            
            
