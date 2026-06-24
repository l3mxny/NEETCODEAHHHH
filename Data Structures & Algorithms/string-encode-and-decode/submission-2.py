class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 
        while i < len(s):
            j = i 
            while s[j] != '#':
                j += 1
            #extract length from beg, might be char in between length + #
            length = int(s[i:j])
            #skip to start of word
            i = j + 1 
            #skip to end of word
            j = length + i 
            res.append(s[i:j])
            #move to next starting word
            i = j 
        return res
