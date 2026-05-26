"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
#easier
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #accounts for all None cases
        copy = {None:None}
        save = head
        #fill in hashmap pass
        while head != None:
            copy[head] = Node(head.val)
            head = head.next
        #save new head node
        result = copy[save]
        #relink
        while save != None:
            copy[save].next = copy[save.next]
            copy[save].random = copy[save.random]
            save = save.next
        return result