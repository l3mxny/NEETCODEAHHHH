#doublyLinkedList

class ListNode:
    def __init__(self,key,val):
    #nodefields
        self.key = key 
        self.val = val
        self.prev = None
        self.next = None 
class LRUCache:
    def __init__(self, capacity: int):
    #fields
        self.capacity = capacity
        self.cache = {}
        #head
        self.left = ListNode(0,0)
        #tail
        self.right = ListNode(0,0)
        #doublyLinkedListFormation
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self,node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    #insetformostrecentlyused(right)
    def insert(self,node):
        node.prev = self.right.prev
        node.next = self.right
        node.prev.next = node
        self.right.prev = node
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            #insert to right end mru
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        #update to be newest
        if key in self.cache:
           self.remove(self.cache[key])
        self.cache[key] = ListNode(key,value)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            #save first
            delete = self.left.next
            #remove head
            self.remove(self.left.next)
           #remove from dict
            del self.cache[delete.key]

    

        
