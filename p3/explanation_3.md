# Rearrange Digits

Once we have a sorted array, finding the 2 numbers whose sum is the
max can be done by alternately appending numbers from the array to
make up the digits of the 2 final integers. This can be done
by looping through the array once in O(N) time. 

But we don't start with a sorted array, so we need to sort the array
in O(N log N) time. Merge sort will do this and once completed, doing
the integer construction in O(N) time will result in a final running
time of O(N log N) + O(N) which is still O(N log N), since O(N log N)
dominates the expression.