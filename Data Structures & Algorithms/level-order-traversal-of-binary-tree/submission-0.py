# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#bfs, queue
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root is None:
            return []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            level = []
            for i in range(level_size):
                level_val = queue.popleft()
                level.append(level_val.val)
                #check if the children exist
                if level_val.left:
                    queue.append(level_val.left)
                if level_val.right:
                    queue.append(level_val.right)
            #add each level before going to next level 
            result.append(level)
        return result




