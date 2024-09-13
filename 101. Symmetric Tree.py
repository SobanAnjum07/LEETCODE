# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        p = root.left
        q = root.right

        return self.helper(p, q)
        

    def helper(self, p, q):

        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        
        if p.val == q.val:

            return self.helper(p.left, q.right) and self.helper(p.right, q.left)

        return False

