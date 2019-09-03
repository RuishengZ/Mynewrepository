# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.depth = 0
        return self.rootDetec(root, self.depth)
            
    def rootDetec(self, root, depth):
        if root:
            depth = depth + 1
            depth = max(self.rootDetec(root.left, depth), self.rootDetec(root.right, depth))
        return depth
        
        

            
        
        