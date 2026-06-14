class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        #strings immutable, slow
        l = 0
        r = 0

        while l != len(word1) and r != len(word2):
            res.append(word1[l])
            res.append(word2[r])
            l += 1
            r += 1
            res += word2[r:]
            res += word1[l:]
            
        return "".join(res)