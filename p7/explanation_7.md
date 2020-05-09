# HTTPRouter Using a Trie

A new node is created for each unique segment that may be introduced when a new
endpoint is added. So the memory requirements for this are O(unique path segments).
Inserting a new endpoint, or searching for one, will take O(length of path segments),
because this represents the depth of the trie for that particular path.



