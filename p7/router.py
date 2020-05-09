from problem_7 import RouteTrie, RouteTrieNode

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routes = RouteTrie()

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        self.routes.insert(path, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        print(self.split_path(path))
        return self.routes.find(path)

    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here 
        if len(path) > 0:
            if path[-1:] == '/':
                path = path[:-1]
            if path[0] == '/':
                path = path[1:]

        path_segs = path.split('/')
        return path_segs


new_router = Router()

new_router.add_handler("/hello/there", "hihandler")

print(new_router.lookup("/hello/there"))

# MyTrie = RouteTrie()
# new_route = "/hello/there"
# MyTrie.insert(new_route)

# print(MyTrie.find("/hello/there"))