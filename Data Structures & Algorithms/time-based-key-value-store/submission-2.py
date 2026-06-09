class TimeMap:

    def __init__(self):
        self.map = {}
    #tuples (pair things, keeps it ordered) 
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
           self.map[key] = []
        self.map[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        res = self.map[key]
        left = 0 
        right = len(res) - 1 
        result = ""
        while left <= right:
            mid = (left + right)//2
            #accessing tuple (0 is value 1 is timestamp)
            if res[mid][1] == timestamp:
               return res[mid][0] 
            #stored matches the case <= 
            elif res[mid][1] < timestamp:
                result = res[mid][0] 
                left = mid + 1
            #stored timestamp is too big, invalid 
            elif res[mid][1] >= timestamp:
                right = mid -1

        #pointers converged to correct pos,use left or right
        return result
            
        
