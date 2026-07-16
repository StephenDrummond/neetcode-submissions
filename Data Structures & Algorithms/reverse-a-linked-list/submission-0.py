# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        cur = head.next
        prev = head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur

            cur = next
        head.next = None
        return prev