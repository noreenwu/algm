class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
        
        
    def suffixes(self, suffix = '', slist = []):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        
#         if self.is_word == True:
#             if len(suffix) > 0:
#                 slist.append(suffix)                

    
        if self.children:
            if self.is_word == True:
                if len(suffix) > 0:
                    slist.append(suffix)   
            
            for k in self.children:
                print("key {}".format(k))
                print("suffix so far {}".format(suffix + k))
                self.children[k].suffixes(suffix + k, slist)
        else:
            slist.append(suffix)
            return
            
        print("slist is {}".format(slist))
        return slist

MyTrie2 = Trie()
wordList = [ "ant", "anthology", "antagonist"]
for w in wordList:
    MyTrie2.insert(w)
MyTrie2.find("ant")
