# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        # ! second approach

        inorder_hash = {v:i for i, v in enumerate(inorder)}

        def helper(l, r):

            if l > r:
                return None
            
            root = TreeNode(postorder.pop())
            indx = inorder_hash[root.val]

            root.right = helper(indx +1, r)
            root.left = helper(l, indx-1)

            return root

        return helper(0, len(inorder)-1)

        # ! first approach
        # if not inorder:
        #     return None

        # root = TreeNode(postorder.pop())
        # ind = inorder.index(root.val)

        # root.right = self.buildTree(inorder[ind+1:], postorder)
        # root.left = self.buildTree(inorder[:ind], postorder)
        
        # return root