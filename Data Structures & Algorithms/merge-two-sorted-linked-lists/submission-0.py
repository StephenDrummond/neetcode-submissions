# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        cur = head

        while list1 or list2:
            if list1 and not list2:
                cur.next = ListNode(list1.val)
                list1 = list1.next
            elif list2 and not list1:
                cur.next = ListNode(list2.val)
                list2 = list2.next
            elif list1 and list1.val <= list2.val:
                cur.next = ListNode(list1.val)
                list1 = list1.next
            elif list2 and list2.val < list1.val:
                cur.next = ListNode(list2.val)
                list2 = list2.next
            cur = cur.next

        return head.next