class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res =[]
        #bool array to track which elements have been picked so far
        boolArray = []
        for i in range(len(nums)):
            boolArray.append(False)

        def backtrack(index, path):
            #base case
            if index == len(nums):
                res.append(path.copy())
            for i in range(len(nums)):
                if not boolArray[i]:
                    #not used 
                    boolArray[i] = True
                    path.append(nums[i])
                    backtrack(index+1,path)
                    path.pop()
                    #reset for next
                    boolArray[i] = False
        backtrack(0,[])
        return res

            
