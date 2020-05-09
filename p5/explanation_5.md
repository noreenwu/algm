# Autocomplete with Tries

A trie is a tree-like structure that allows for efficiently inserting
and looking up words in O(length of word) time, with storage needs
depending on the number of unique character combinations or words
O(alphabet_size * key_length * num_entries). The lookup efficiency
compares favorably to that of a hash and the storage efficiency
is better than that of a hash, which cannot take advantage of the
replication of prefixes that many words share.

For a use case like autocompletion, the autocompletion possibilities
may be determined by recursively traversing all nodes below the
node representing the prefix that has already been typed in. The
complexity for determining all suffixes will be O(num_suffixes * len_suffixes),
which will decrease as more letters are typed in. At the top
of the tree (worst case), the complexity of finding all suffixes
will be O(num_words * length_words).



