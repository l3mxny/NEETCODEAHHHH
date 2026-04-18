#neetcode solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        #auto creates empty list if key doesnt exist
        for s in strs:
            count = [0] * 26
            #creates a list of 26 0s
            for c in s:
                count[ord(c) - ord('a')] += 1
                #converts character to ASCII number , subtracts by measuring distace from a 
                #and increments
            res[tuple(count)].append(s)
        return list(res.values())


        #res = {
    #(1,0,0,0,1,...): ["eat", "tea", "ate"],
    #(1,1,0,0,0,...): ["bat"],
    #}