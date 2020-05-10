# Max and Min in an Unsorted Array

If the array were sorted, we could take the 0th element as the min and
the length-1st element as the max. But it is not sorted, it's random.
The fastest sorting algorithms O(N log N), so we can beat that by
setting an initial min and an initial max value to the first element
in the array and then simply traverse the array once, checking to see if 
each value has beaten either the min or the max. Because we only traverse
the array once, the running time is O(N). Additional space for the
array was not required: O(1).



