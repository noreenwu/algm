# A RouteTrie stores our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        self.root = RouteTrieNode()

    def insert(self, path_segs, handler):
        # Recursively add nodes that are specified in path_segs.
        # The handler is assigned to only the leaf (deepest) node of this path
        current_node = self.root

        for a in path_segs:
            if a not in current_node.children:
                current_node.children[a] = RouteTrieNode()
            current_node = current_node.children[a]
            
        current_node.handler = handler            
        current_node.is_route = True

    def find(self, path_segs):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root

        for a in path_segs:
            if a not in current_node.children:
                return None          # match not found
            current_node = current_node.children[a]
            
        return current_node.handler   

# A RouteTrieNode stores an associated handler.
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


# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, homepage='homepage handler'):
        # Create a new RouteTrie for holding our routes
        self.routes = RouteTrie()
        self.add_handler('/', homepage)

    def add_handler(self, path, handler):
        # Add a handler for a path:
        # split the path and pass the path segments as a list to the RouteTrie
        path_segs = self.split_path(path)
        self.routes.insert(path_segs, handler)

    def lookup(self, path):
        # lookup path (by segments) and return the associated handler
        # if not found, return "not found handler"
        path_segs = self.split_path(path)
        if self.routes.find(path_segs) is None:
            return "not found handler"

        return self.routes.find(path_segs)

    def split_path(self, path):
        # split the path into segments for both the add_handler and loopup functions
        if len(path) > 0:
            if path[-1:] == '/':
                path = path[:-1]
            if len(path) > 0 and path[0] == '/':
                path = path[1:]

        path_segs = path.split('/')
        if len(path_segs) == 0:
            path_segs = [ '/']

        return path_segs


new_router = Router()

new_router.add_handler("/home/about", "about handler")

print("\tHandler: {}\n".format(new_router.lookup("/home/about"))) # about handler

print("\tHandler: {}\n".format(new_router.lookup("/home/about/"))) # about handler (ignores trailing /)

new_router.add_handler("/home/about/me", "about me handler")

print("\tHandler: {}\n".format(new_router.lookup("/home/about/me"))) # about me handler

new_router.add_handler("/12/14/19/news", "news handler")

print("\tHandler: {}\n".format(new_router.lookup("/12/14/19/news"))) # news handler

print("\tHandler: {}\n".format(new_router.lookup("")))  # homepagehandler

print("\tthis route is not defined and lookup returns: {}\n".format(new_router.lookup("/something/else")))
    # not found handler
