# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#preorder: node left right
# in order: left node right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #index of preorder
        self.curr = 0
        #keep track of inorder, helps rebuild by tell where to split
        self.map = {}
        l = 0 
        r = len(inorder)-1
        for i in range(len(inorder)):
            self.map[inorder[i]] = i
        return self.buildTreeHelper(preorder,inorder,l,r)

    def buildTreeHelper(self, preorder, inorder, l , r ):
        if l > r:
            return 
        #start new nodes
        root =  TreeNode(preorder[self.curr])
        mid = self.map[root.val]
        self.curr += 1
        #bst range trick
        root.left = self.buildTreeHelper(preorder,inorder,l,mid-1)
        root.right = self.buildTreeHelper(preorder,inorder,mid+1,r)
        return root