class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
p = TreeNode(1)
pl = TreeNode(2)
# pr = TreeNode(3)
q = TreeNode(1)
ql = TreeNode(None)
qr = TreeNode(2)

p.left = pl
# p.right = pr
q.left = ql
q.right = qr

class Solution:
    def isSameTree(self, p, q):
        if p and q:
            print(p.val, q.val)
            if p.val == q.val:
                self.isSameTree(p.left, q.left)
                self.isSameTree(p.right, q.right)
                return 1
            
            else:
                return 0
                
        elif p == q:
            return 1
        else:
            return 0
            
x = Solution()
x.isSameTree(p,q)