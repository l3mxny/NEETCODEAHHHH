class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = {}
        for i in strs:
            if tuple(sorted(i)) in ret:
                ret[tuple(sorted(i))].append(i) 
            else:
                ret[tuple(sorted(i))] = [i]
        return list(ret.values())