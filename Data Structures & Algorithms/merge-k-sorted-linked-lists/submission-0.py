# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, n1, n2):
        head = ListNode()
        cur = head
        while n1 and n2:
            if n1.val <= n2.val:
                cur.next = n1
                n1 = n1.next
            else:
                cur.next = n2
                n2 = n2.next
            cur = cur.next
        if n1:
            cur.next = n1
        elif n2:
            cur.next = n2
        return head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        k = len(lists)

        for i in range(k):
            head.next = self.merge(head.next, lists[i])


        return head.next