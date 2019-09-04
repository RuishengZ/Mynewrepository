# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.currentStr = ""
        self.list = []
        self.flag = 0
        self.Path_find(self.currentStr, self.list, root, self.flag)
        
        return self.list
            
        
    def Path_find(self, Str, Ls, root, flag):
        if root:
            if not root.left and not root.right:
                Str += "->"
                Str += str(root.val)
                if len(Str) == 3:
                    Ls.append(Str[-1])
                else:
                    Ls.append(Str)
                    Str = Str[:-1]
            else:
                if flag == 1:
                    Str += "->"
                flag = 1
                Str += str(root.val)
                self.Path_find(Str, Ls, root.left, flag)
                self.Path_find(Str, Ls, root.right, flag)

        

        
        return Str, Ls
            
        