# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast, slow = head, head
        new_head = None
        group_tail = None

        while True:
            cur = fast
            for _ in range(k):
                if not fast:
                    if slow:
                        group_tail.next = slow
                    return new_head
                fast = fast.next
            
            prev = None
            while slow != fast:
                nxt = slow.next
                slow.next = prev
                prev = slow
                slow = nxt
            
            if group_tail:
                group_tail.next = prev
            else:
                new_head = prev
            
            group_tail = cur
