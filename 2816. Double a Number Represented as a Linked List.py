# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_list = self.reverse_list(head)

        carry = 0
        curr, previous = reversed_list, None

        while curr:

            new_val = curr.val * 2 + carry
            curr.val = new_val % 10
            carry = 1 if new_val > 9 else 0
            previous, curr = curr, curr.next

        if carry:
            previous.next = ListNode(carry)

        result = self.reverse_list(reversed_list)

        return result
    
    def reverse_list(self, node):

        previous, curr = None, node

        while curr:
            
            next_node = curr.next

            curr.next = previous

            previous, curr = curr, next_node
        
        return previous

            
