# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#same structure as binary level order traversal
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root is None:
            return []
        queue = deque([root])
        while queue: 
            level_size = len(queue)
            for i in range(len(queue)):
                level_val = queue.popleft()
                if i == level_size - 1:
                    result.append(level_val.val)
                if level_val.left:
                    queue.append(level_val.left)
                if level_val.right:
                    queue.append(level_val.right)
        return result
                    