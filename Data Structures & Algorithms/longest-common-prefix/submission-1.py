class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #make one as the checker, accounts for all lengths
        for i in range(len(strs[0])):
            for s in strs:
                if i >= len(s) or s[i] != strs[0][i]:
                    #slice
                    return strs[0][0:i]
        return strs[0]