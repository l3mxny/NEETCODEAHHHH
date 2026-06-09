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
        while left < right:
            mid = (left + right)//2
            #accessing tuple (0 is value 1 is timestamp)
            if timestamp == res[mid][1]:
               return res[mid][0] 
            elif timestamp > res[mid][1]:
                left = mid + 1
            elif timestamp <= res[mid][1]:
                right = mid -1
        #no valid timestamp
        if res[left][1] > timestamp : 
            return ""
        #pointers converged to correct pos,use left or right
        return res[left][0]
            
        
