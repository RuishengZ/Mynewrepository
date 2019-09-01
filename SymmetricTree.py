# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def SymmetricDec(self, left: TreeNode, right: TreeNode):

        if not left and not right:
            return 1
        if not left and right:
            return 0
        if left and not right:
            return 0
        if left.val != right.val:
            return 0

        return self.SymmetricDec(left.left, right.right) and self.SymmetricDec(left.right, right.left)   
    
    def isSymmetric(self, root: TreeNode) -> bool:
        if root:
            return self.SymmetricDec(root.left, root.right)
        else:
            return True
        
    
 
           


        
            
            
        