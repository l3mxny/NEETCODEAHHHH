#list faster
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        l = 0
        r = 0

        llen = len(word1)
        rlen= len(word2)

        while l < llen or r < rlen:
            #or method, adds seperately
            if l < llen:
                res.append(word1[l])
            if r < rlen:
                res.append(word2[r])
            l += 1
            r += 1
        return "".join(res)

       
