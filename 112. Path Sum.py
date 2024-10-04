# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def traversal(root, sum_ = 0):
            if root is None: 
                return False
            
            sum_ += root.val

            if root.left is None and root.right is None:
                if sum_ == targetSum: 
                    return True

                else:
                    sum_ -= root.val
                    return False
            
            return traversal(root.left, sum_) or traversal(root.right, sum_)

        return traversal(root)


