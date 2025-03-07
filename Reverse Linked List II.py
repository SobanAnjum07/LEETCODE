# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy


        for _ in range(left-1):
            prev = prev.next

        cur = prev.next
        # next_node = None
        for _ in range(right-left+1):

            next_node = cur.next
            cur.next = prev.next
            prev.next = cur
            cur = next_node

        temp = prev
        for _ in range(right-left +1):
            temp =temp.next

        temp.next = cur

        return head