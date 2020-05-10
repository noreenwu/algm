# HTTPRouter Using a Trie

A new node is created for each unique segment that may be introduced when a new
endpoint is added. So the memory requirements for this are O(unique path segments).
Inserting a new endpoint, or searching for one, will take O(length of path segments),
because this represents the depth of the trie for that particular path.


## Time and Space Complexity of Each Function

### split_path
Both add_handler and lookup depend on split_path, which takes the specified
path and splits it into path segments. This operation is O(N), where N is
the number of characters in the path, because it is necessary to traverse the 
entire path looking for the '/' character, capturing each segment each time
a '/' is encountered. Eliminating leading and trailing '/' are both O(1)
operations because we do not traverse the entire list, but access the first
and last characters respectively, and chop them off if they are equal to '/'.

Space-wise, split_path is going to create an array as large as the number
of segments there are per path, multiplied times the worst case size of
a path segment, or O(longest_segment_length * number_of_segments). However, these
path segment arrays are temporary; they are used in the insertion and
find operations, but once these operations complete, they are cleaned up. 

### add_handler

To add a new handler to the Router, split_path is first used. Then,
in RouteTrie, we traverse the trie, as long as there is a match with
the specified path (path segments). The time complexity of this operation
is equal to the number of segments in the original path, as we loop
through, either confirming the previous existence of the path segment
or creating a new one, until all the specified path segments have
been reached, at which point we save the handler. O(number of path segments
in specified path). An example: '/home/about/me' would have time
complexity O(3).

Space-wise, each path will consume a new node for each segment. If there
are a lot of repeating segments (e.g. a lot of endpoints that begin
with '/about' or '/12/28/14'), then some space will be saved, but in the
worst case, each path segment is unique and the total space complexity
will end up being O(number of path segments in all of the routes).


### lookup

Looking up an existing endpoint is similar to adding one. First,
use split_path to get an array of path segments. Then traverse
the trie until a mismatch is found or (worst case), until all
the path segments are checked. If each path segment has a match,
then return the handler. This process takes O(N) steps, where N
is the number of segments in the path.

Space-wise, a lookup does not create any additional space other
than the temporary array described in split_path. The traversal
to find an existing set of nodes does not require more nodes
to be created, so the space complexity is O(1).


## Summary

I would consider the time complexity of insertion and lookup 
of new endpoints to be O(1), because generally endpoints are
not longer than, say, 3 path segments, so this is actually
comparable to that of a hash lookup.

The space complexity is equal to O(unique path segments * size of trie node).
Compared to a hash, there will be savings in space due to shared
path segments that may occur across all of the routes for a single
website.

Furthermore, this data structure is a better match for
the representation and retrieval of endpoints, as looking for
the path segments is similar to doing a cd into a subdirectory,
one at a time. A hash would likely store the entire path
as a key and would not allow as graceful a printout of all
endpoints, if one were desired. Also, in the case of a news
site, where a lot of articles may be under the same date structure
for each news day, the space savings will accumulate.

