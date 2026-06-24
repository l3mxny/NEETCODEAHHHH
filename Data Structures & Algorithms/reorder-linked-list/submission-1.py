# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next
            if fast.next != None:
                fast = fast.next
        second = slow.next
        slow.next = None
        prev = None
        #save flip move
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        #merge
        first = head
        second = prev
        #save connect move
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        

        