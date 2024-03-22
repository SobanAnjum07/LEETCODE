class Solution:
    def reverseList(self, head):

        previous = None
        next_node = None

        cur = head
        while cur:
            next_node = cur.next
            cur.next = previous
            previous = cur
            cur = next_node
        return previous