#ime
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = []
        for i in range(len(position)):
            cars.append([position[i],speed[i]])
        cars.sort()
        for i in range(len(position)-1,-1,-1):
            time = (target - cars[i][0]) / cars[i][1]
            #cant pass it
            if stack and time <= stack[-1]:
                stack.pop() 
            stack.append(time)
        return len(stack)
