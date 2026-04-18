#NEETCODE SOLUTION 2 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        #returns empty list if no list 
        for s in strs:
            sortedS = ''.join(sorted(s))
            #sorts, then joins it back 
            res[sortedS].append(s)
            #adds to the dict 
        return list(res.values())