# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#msolution
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        slow = head
        fast = head.next
        while fast != None:
            #cycle detected
            if slow == fast: 
                return True
            slow = slow.next
            #is it safe to keep going in list
            if fast.next != None:
                fast = fast.next.next
            else:
                return False
        return False