# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()

    def insert(self, path_segs, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path

        # ary = path.split('/')
        current_node = self.root

        for a in path_segs:
            print("handling {}".format(a))
            if a not in current_node.children:
                current_node.children[a] = RouteTrieNode()
            current_node = current_node.children[a]
            
        current_node.handler = handler            
        current_node.is_route = True

    def find(self, path_segs):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        
        # ary = path.split('/')

        for a in path_segs:
            if a not in current_node.children:
                return False
            current_node = current_node.children[a]
            
        return current_node        

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler="handler"):
        # Initialize the node with children as before, plus a handler
        self.is_route = False
        self.children = {}
        self.handler = ""

    def insert(self, route, handler):
        # Insert the node as before
        self.children[route] = RouteTrieNode()
        self.handler = handler


