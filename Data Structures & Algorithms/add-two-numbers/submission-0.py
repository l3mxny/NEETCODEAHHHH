# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        carry = 0 
        add = 0
        while l1 or l2 or carry:
            #node exists
            if l1:
                v1 = l1.val
            #no more nodes
            else:
                v1 = 0
            if l2:
                v2 = l2.val
            else:
                v2 = 0
            #add
            add = v1 + v2 + carry
            if add > 9 :
                carry = add // 10 
            else:
                carry = 0 
            #digit (apart from carry)
            digit = add % 10 
            cur.next = ListNode(digit)
            cur = cur.next
            #advance l1 and l2 if exist
            if l1 and l2 : 
                l1 = l1.next
                l2 = l2.next
        return dummy.next
