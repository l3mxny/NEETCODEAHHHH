# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#interval with upper lower limits 
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #initial no lower and upper bound
        return self.isValidBSTHelper(root, float("-inf") , float("inf"))    

    def isValidBSTHelper(self, root, min, max) :
        if root is None:
            return True
        if root.val <= min:
            return False
        if root.val >= max:
            return False
        #go left, current becomes max, go right, current becomes min (everything on right is greater than it)
        return self.isValidBSTHelper(root.left,min,root.val) and self.isValidBSTHelper(root.right,root.val,max)
      