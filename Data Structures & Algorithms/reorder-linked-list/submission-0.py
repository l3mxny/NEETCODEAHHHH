# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#mysolution
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find midpoint
        slow = head 
        fast = head.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        #slow is now at midpoint
        start2 = slow.next
        slow.next = None
        #reversal of start2 list
        cur = start2
        prev = None
        while cur != None:   
            next = cur.next 
            cur.next = prev
            prev = cur
            cur = next 
        #prev is pointing to start of list2
        #merging
        while head != None and prev != None:
            #point to start of two list
            list1 = head.next
            list2 = prev.next
            #rewire
            head.next = prev
            prev.next = list1
            #advance
            head = list1
            prev = list2
        

