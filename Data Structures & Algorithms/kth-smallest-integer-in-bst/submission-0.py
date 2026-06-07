# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#inorder dfs, count as local 
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #count as instance var 
        self.count = k 
        return self.kthSmallestHelper(root,k)

    def kthSmallestHelper(self,root,k):
        if root is None:
            return None
        res = self.kthSmallestHelper(root.left,k)
        if res is not None:
            return res
        self.count -= 1
        if self.count == 0:
            return root.val
        return self.kthSmallestHelper(root.right, k)