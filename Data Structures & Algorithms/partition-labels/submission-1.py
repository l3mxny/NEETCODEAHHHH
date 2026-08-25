class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = {}
        res = []
        size = 0 
        for i in range(len(s)):
            hashmap[s[i]] = i 

        end = 0 
        for i in range(len(s)):
            size += 1
            end = max(end,hashmap[s[i]])
            if i == end:
                res.append(size)
                size = 0 
        return res


        