# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next or k == 0:
            return head

        len_ = 1
        tail = head
        while tail.next:
            tail = tail.next
            len_ += 1

        k = k % len_

        if k == 0:
            return head

        tail.next = head

        steps = len_ - k 
        prev = tail
        for _ in range(steps):
            prev = prev.next

        new_head = prev.next
        prev.next = None

        return new_head
        