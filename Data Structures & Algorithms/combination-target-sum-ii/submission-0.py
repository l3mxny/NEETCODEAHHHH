#passed in array may contain duplicates 
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        #sort, for loop handles
        candidates.sort()
        def backtrack(index, path): 
            #base cases 
            if sum(path) > target:
                return   
            if sum(path) == target:
                res.append(path.copy())
                return
            #make it last so it cant be skipped over 
            if index >= len(candidates):
                return
            #include
            path.append(candidates[index])
            backtrack(index+1, path)
            path.pop()
            #skip
            while index + 1 < len(candidates) and candidates[index] == candidates[index+1]:
                #skip through all duplicates
                index += 1
            backtrack(index+1, path)
        backtrack(0,[])
        return res
                