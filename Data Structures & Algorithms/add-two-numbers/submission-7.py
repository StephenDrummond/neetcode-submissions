# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode()
        cur = head
        while l1 or l2 or carry:
            
            x, y = 0, 0
            if l1:
                x = l1.val
                l1 = l1.next
            if l2:
                y = l2.val
                l2 = l2.next
            s = x + y + carry
            if s > 9:
                s = s % 10
                carry = 1
            else:
                carry = 0
            cur.next = ListNode(s)
            cur = cur.next

        return head.next
            