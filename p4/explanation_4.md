# Dutch National Flag Problem

To sort an array consisting only of the values 0, 1, 2 in O(N) time with
O(N) space and in a single pass, walk through the array moving "0" values
and "2" values into their correct locations.

While keeping track of where the "next 0" and "next 2" should go, the
list is traversed. If a "0" or "2" is encountered during traversal, it is 
swapped with the value in the "next 0" or "next 2" position. This goes on 
until the traversal is complete, at which point the array is in sorted order. 

This single traversal may take less than O(N) if "2" values are encountered 
during traversal, allowing the "next 2" position to move down from the last element in the list. We don't need to traverse the list past the "next 2" position, because everything above that point is a "2" and already in the right place.


