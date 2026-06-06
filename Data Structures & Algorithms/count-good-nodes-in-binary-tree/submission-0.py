# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        max = root.val
        return self.goodNodesHelper(root,max)

    def goodNodesHelper(self,root,max):
        if root is None:
            return 0 
        #good nodes
        if root.val >= max:
            max = root.val 
            return 1 + self.goodNodesHelper(root.left,max) + self.goodNodesHelper(root.right,max)
        else:
            return self.goodNodesHelper(root.left,max ) + self.goodNodesHelper(root.right, max)