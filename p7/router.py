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
        path_segs = self.split_path(path)
        print("adding {}".format(path_segs))
        self.routes.insert(path_segs, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_segs = self.split_path(path)
        print("looking up {}".format(path_segs))
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

new_router.add_handler("/hello/there", "hihandler")

print("\tHandler: {}\n".format(new_router.lookup("/hello/there")))

new_router.add_handler("/hello/about", "abouthandler")

print("\tHandler: {}\n".format(new_router.lookup("/hello/about")))

new_router.add_handler("/12/14/19/news", "newshandler")

print("\tHandler: {}\n".format(new_router.lookup("/12/14/19/news")))

new_router.add_handler("/", "root")

print("\tHandler: {}\n".format(new_router.lookup("")))

print("\tthis route is not defined and lookup returns: {}\n".format(new_router.lookup("/something/else")))