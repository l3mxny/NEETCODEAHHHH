#bucket hashing
class MyHashSet:

    def __init__(self):
        self.array = []
        for i in range(1000):
            self.array.append([])

    def add(self, key: int) -> None:
        index = key % len(self.array)
        #no dupliates 
        if key in self.array[index]:
            return None
        else:
            self.array[index].append(key)

    def remove(self, key: int) -> None:
        index = key % len(self.array)
        if key in self.array[index]:
            self.array[index].remove(key)
        else:
            return None
        

    def contains(self, key: int) -> bool:
        index = key % len(self.array)
        if key in self.array[index]:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)