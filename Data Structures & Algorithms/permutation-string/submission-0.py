#mysolution
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowLength = len(s1)
        left = 0 
        right = windowLength
        dicts1 = {}
        #s1 hashmap
        for char in s1:
            if char not in dicts1:
                dicts1[char] = 0
            dicts1[char] += 1
        dicts2 ={}
        #s2 hashmap for current window
        for char in s2[left:right]:
            if char not in dicts2:
                dicts2[char] = 0
            dicts2[char] += 1

        if dicts1==dicts2:
            return True
        #changing window until end of s2      
        for i in range(windowLength, len(s2)):
            if s2[i] not in dicts2:
                dicts2[s2[i]] = 0
            #for incoming char
            dicts2[s2[i]] += 1
            #for leaving char
            dicts2[s2[i-windowLength]] -= 1
            #remove from hashmap is count is 0 for leaving char 
            if dicts2[s2[i-windowLength]] == 0:
                del dicts2[s2[i-windowLength]]
            if dicts1==dicts2:
                return True
        return False
    