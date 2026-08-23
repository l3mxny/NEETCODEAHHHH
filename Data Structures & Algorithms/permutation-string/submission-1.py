class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        hashCountS2 = {}
        hashCountS1 = {}

        for ch in s1:
            hashCountS1[ch] = hashCountS1.get(ch,0) + 1

        l = 0 
        r = 0 

        while r < len(s2):
            hashCountS2[s2[r]] = hashCountS2.get(s2[r],0) + 1
            if (r-l+1) > len(s1):
                if hashCountS2[s2[l]] == 1:
                    del hashCountS2[s2[l]]
                else:
                    hashCountS2[s2[l]] -= 1
                l += 1
            if (r-l+1) == len(s1):
                if hashCountS2 == hashCountS1:
                    return True
            r += 1
        return False

        

        