# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        node1, node2 = head, head.next
        head, previous = node2, node1

        while node2:
            node1.next, node2.next = node2.next, node1
            if node2 != head:
                previous.next, previous = node2, node1
            node1 = node1.next

            if not node1:
                return head
            node2 = node1.next
        return head
