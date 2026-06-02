# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#mysol
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #case1: p and q less than current, go left 
        if ( p.val < root.val and q.val < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        #case2: p and q greater than current, go right
        elif (p.val > root.val and q.val > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        #case3: p and q equal the current 
        else:
            return root