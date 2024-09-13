# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        count = 0
        def traversal(r, count):

            if not r:
                return count

            return max(traversal(r.left, count + 1), traversal(r.right, count + 1))
        return traversal(root, count)
