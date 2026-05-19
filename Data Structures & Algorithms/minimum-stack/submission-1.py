#mysolution
class MinStack:

    def __init__(self):
        #initiate stacks
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        #add to main stack
        self.stack.append(val)
        #chck the min stack, only add the mininum, compare to current min @ top
        if len(self.minStack) == 0:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))
    #pop both
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
    #return the one on the top for the main stack
    def top(self) -> int:
        return self.stack[-1]
    #return one on the top for min stack
    def getMin(self) -> int:
        return self.minStack[-1]
        
