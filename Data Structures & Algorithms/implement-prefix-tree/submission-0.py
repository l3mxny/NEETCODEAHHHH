#learningTries.
class PrefixTree:

    def __init__(self):
        # 'a' : PrefixTree()
        self.children = {}
        self.endOfWord = False
       

    def insert(self, word: str) -> None:
        cur = self #current object
        for c in word:
            #insert if not in word nodes
            if c not in cur.children:
                cur.children[c] = PrefixTree()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self
        for c in word:
            if c not in cur.children: 
                return False
            cur = cur.children[c]
        #it is a word by checking mark @ end
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for c in prefix:
            if c not in cur.children:
                return false
            cur = cur.children[c]
        return True
        
        