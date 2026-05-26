"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
#mysolution
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #create copy
        copy = {}
        headSave = head
        headReturn = head
        while head != None:
            copy[head] = Node(head.val)
            head = head.next
        #refigure next and random nodes
        while headSave != None:
            if headSave.next == None:
                copy[headSave].next = None
            else:
                copy[headSave].next = copy[headSave.next]
            if headSave.random == None:
                copy[headSave].random = None
            else:
                copy[headSave].random = copy[headSave.random]
            headSave = headSave.next
        return copy[headReturn]
           