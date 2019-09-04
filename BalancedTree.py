# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.Ldepth = 0
        self.Rdepth = 0
        if not root:
            return True
        else:
            L = self.BalanceDet(root.left, 0)
            R = self.BalanceDet(root.right, 0)
            if abs(L-R) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
                return True
            else:
                return False
            
    
    def BalanceDet(self, root, depth):
        if root:
            depth = depth + 1
            depth = max(self.BalanceDet(root.left, depth), self.BalanceDet(root.right, depth))
            
        return depth
    
    
    
        