class WordDictionary:

    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def addWord(self, word: str) -> None:
        cur = self
        for c in word:
            if c not in cur.children:
                #create node for children val
                cur.children[c] = WordDictionary()
                #move cur forward
            cur = cur.children[c]
        #reached end 
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self
        for i in range(len(word)):
            if word[i] == '.':
                #ask every child, match with word map it connects to
                for child in cur.children.values():
                    if child.search(word[i+1:]):
                        return True
                return False
            #if it is regular character
            else:
                #check if its in the dict first
                if word[i] in cur.children:
                    cur = cur.children[word[i]]
                else:
                    return False
        return cur.endOfWord
                    
            
