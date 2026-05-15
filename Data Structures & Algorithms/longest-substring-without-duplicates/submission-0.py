#mysolution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        count = 0
        maxCount = 0;
        dupe = set()
        for i in range(len(s)): 
        #when i is in the set, means duplicate found, keep looping and removing
            while s[i] in dupe:
                dupe.remove(s[left])
                left +=1
        #when not in the set, add to set and count
        
            dupe.add(s[i])
            count = i - left + 1
            if maxCount < count:
                maxCount = count
        return maxCount

