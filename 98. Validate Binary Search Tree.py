# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        res = []
        
        def dfs(root, res):
            
            if root is None :
                return 
            
            if root:
                
                dfs(root.left, res)
                
                res.append(root.val)
                
                dfs(root.right, res)
             
            return res
                
            
        res = (dfs(root, res))
        def validate(res):
            for i in range(1, len(res)):
                if res[i] <= res[i-1]:
                    return False
            return True
        return validate (res)
        
