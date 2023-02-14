# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = l1.head
        node2 = l2.head
        while node1 is not None:
            node1.val += node2.val
            yield node1, node2
            node2 = node2.next
            node1 = node1.next
        return l1
