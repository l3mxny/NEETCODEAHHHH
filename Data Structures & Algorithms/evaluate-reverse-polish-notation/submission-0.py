class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result= []  
        #loop over list
        for token in tokens:
            #check if its a number
            if token not in ["+","-","*","/"]:
                result.append(int(token))
            else:
                first = result.pop()
                second = result.pop()
                if token == "+":
                    result.append(first + second)
                elif token == "-":
                    result.append(second - first)
                elif token == "*":
                    result.append(first * second)
                else: 
                    result.append(int(second / first))
        
        return result.pop()
