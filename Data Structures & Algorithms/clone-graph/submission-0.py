"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldtoMap = {}
        if node is None:
            return None
        def dfs(node):
            #copy
            clone = Node(node.val)
            #add
            oldtoMap[node] = clone
            #check
            for n in node.neighbors:
                if n not in oldtoMap:
                    dfs(n)
                #already added, connect with cloned
                clone.neighbors.append(oldtoMap[n])
            return clone
        return dfs(node)