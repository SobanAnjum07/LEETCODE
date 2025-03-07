# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
    # Input: head = [4,5,1,9], node = 5
    # Output: [4,1,9]
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        if node and node.next:
            node.val = node.next.val
            node.next = node.next.next