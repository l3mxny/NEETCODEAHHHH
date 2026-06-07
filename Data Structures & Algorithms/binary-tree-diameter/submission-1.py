# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#dfs 
#mysolution
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        self.maximum = 0 
        #run dfs
        self.diameterOfBinaryTreeHelper(root)
        #best diameter
        return self.maximum 
    

    def diameterOfBinaryTreeHelper(self, root):
        if root == None:
            return 0 
        #height
        leftDepth = self.diameterOfBinaryTreeHelper(root.left)
        rightDepth = self.diameterOfBinaryTreeHelper(root.right)
        #calc diameter
        self.maximum = max(self.maximum, leftDepth + rightDepth)
        #return height
        return 1 + max(leftDepth,rightDepth)
        
        