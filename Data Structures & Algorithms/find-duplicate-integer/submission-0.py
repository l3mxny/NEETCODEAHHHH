#identify cycle via array. linkedlist. floyds. ??
# treat each value as a pointer to the next index
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        #find entry point of cycle, start @ same do while
        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if slow == fast:
                break
        #cycle detected exit 
        #phase2
        slow = 0 
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
