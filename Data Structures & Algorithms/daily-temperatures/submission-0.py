class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        #prefil for loop 
        result = [0] * len(temperatures)
        for i in range(len(temperatures)): 
            #stack is truthy when its filled
            #current i in temp is gerater than top of stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                #most recent greatest number on stack
                answer = stack.pop()
                #fill in result array 
                result[answer] = i - answer
            #monotomic stack order
            stack.append(i)

        return result