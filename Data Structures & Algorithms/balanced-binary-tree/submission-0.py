# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#tuplemethod
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_Bal, height = self.isBalancedHelper(root)
        return is_Bal


    def isBalancedHelper(self,root):
        #base
        if root == None:
            return True, 0
        is_BalLeft, heightLeft = self.isBalancedHelper(root.left)
        is_BalRight, heightRight = self.isBalancedHelper(root.right)
        #are left, right balanced and  <= 1
        is_Bal = is_BalLeft and is_BalRight and abs(heightLeft - heightRight) <= 1
        return is_Bal, 1 + max(heightLeft, heightRight)