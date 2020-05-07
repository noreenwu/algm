class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
        
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        current_node = self
        
        res = ''
        for char in suffix:
            print (char)
            res += char
            current_node = current_node.children[char]
            
        print(res)
        return "hello"

MyTrie2 = Trie()
wordList = [ "ant", "anthology", "antagonist"]
for w in wordList:
    MyTrie2.insert(w)
MyTrie2.find("ant")
