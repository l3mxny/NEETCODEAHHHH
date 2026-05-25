# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#mysolution
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #find length
        length = 0
        headSave = head
        headReturn = head
        while head != None:
            length+=1
            head = head.next
        #head removal edge case:
        if length == n:
            return headSave.next
        #loop until target
        count = 0
        while count != (length-n-1):
            count += 1
            headSave = headSave.next
        #relink 
        headSave.next = headSave.next.next
        return headReturn