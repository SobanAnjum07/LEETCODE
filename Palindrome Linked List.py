# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if not head or not head.next:
            return True
        
        
        # finding the half with slow and fast pointer
        
        slow , fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        
        # now reversing the list
        
        prev = None
        
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
            
            
        left, right = head, prev
        
        while right:
            
            if right.val != left.val:
                return False
            
            right = right.next
            left = left.next
            
        return True
            