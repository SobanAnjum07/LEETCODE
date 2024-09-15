# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right   
        
from collections import defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        self.dic = defaultdict(list)

        def fun (r, depth):

            self.dic[depth].append(r.val)
            if r.left: fun(r.left, depth + 1)
            if r.right: fun(r.right, depth + 1)

        if root : fun(root, 0)

        return [self.dic[i] for i in sorted(self.dic.keys())]
