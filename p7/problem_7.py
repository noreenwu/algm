# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()

    def insert(self, path_segs, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path

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
                return None
            current_node = current_node.children[a]
            
        return current_node.handler   

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


# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, homepage='homepage handler'):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routes = RouteTrie()
        self.add_handler('/', homepage)

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_segs = self.split_path(path)
        # print("adding {}".format(path_segs))
        self.routes.insert(path_segs, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_segs = self.split_path(path)
        # print("looking up {}".format(path_segs))
        if self.routes.find(path_segs) is None:
            return "not found handler"

        return self.routes.find(path_segs)

    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here 
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
