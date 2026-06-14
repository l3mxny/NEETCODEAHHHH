class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(index, path):
            if sum(path) > target:
                return
            if index == len(nums):
                if sum(path) == target:
                    res.append(path.copy())
                return
            #case 1 include path
            path.append(nums[index])
            backtrack(index, path)
            path.pop()

            #case 2 skip, dont include in path
            backtrack(index+1, path)
        backtrack(0,[])
        return res

        
        
        
        


                
                