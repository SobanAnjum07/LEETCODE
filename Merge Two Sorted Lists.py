# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        pnt_1 = list1
        pnt_2 = list2
        dummy_node = ListNode()

        
        app_node = dummy_node
        
        while pnt_1 and pnt_2:
            
            if pnt_1.val < pnt_2.val:
                app_node.next = ListNode(pnt_1.val)
                pnt_1 = pnt_1.next
                
            else:
                app_node.next = ListNode(pnt_2.val)
                pnt_2 = pnt_2.next
                
            app_node = app_node.next
        
        app_node.next = pnt_1 if pnt_1 else pnt_2
            
        return dummy_node.next
            
            
            