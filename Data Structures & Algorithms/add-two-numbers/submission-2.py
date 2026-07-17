# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        cur = head
        carry = 0
        while l1 or l2 or carry:
            l1v = l1.val if l1 else 0
            l2v = l2.val if l2 else 0
            sm = l1v + l2v + carry
            if sm > 9:
                carry = 1
                sm = sm - 10
            else:
                carry = 0
            cur.val = sm
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            if carry or l1 or l2:
                cur.next = ListNode()
            cur = cur.next
        
        return head