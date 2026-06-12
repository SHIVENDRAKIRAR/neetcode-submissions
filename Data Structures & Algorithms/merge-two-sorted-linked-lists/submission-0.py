# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        curr1 = list1
        curr2 = list2

        # Set initial head
        if curr1.val <= curr2.val:
            head = curr1
            curr1 = curr1.next
        else:
            head = curr2
            curr2 = curr2.next

        tail = head  # pointer used to build list

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                tail.next = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2
                curr2 = curr2.next

            tail = tail.next  # move forward

        # Attach remaining nodes
        if curr1:
            tail.next = curr1

        if curr2:
            tail.next = curr2

        return head
            
                      