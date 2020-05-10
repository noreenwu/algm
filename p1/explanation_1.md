## Find Closest Square Root of Provided Number

The first solution to come to mind may be to try each integer, from 1 on up,
until the integer multiplied times itself yields the target number or goes over.
If it goes over, then the previous number, the first one to not go over,
would be the answer.

As numbers get larger, the fraction of the numbers that have to be tested compared
to the size of the number becomes smaller and smaller. So not terrible, less than O(N) 
time complexity, but there is a better way, which is to do a binary search for the answer.

## Binary Search Solution

Take half of the provided number as the starting point and check if its square
is higher or lower than the target. If higher, then search the smaller of the
two spaces. Repeat halving the range of numbers to search, always checking
if the midpoint of that range is the answer. This way of continuously diminishing
the search space by half means that we will get the solution in O(log N) tries.


# Space Complexity

No additional storage is required to perform this algorithm, other than 
the minimal space required to store the working variables, lower, upper, mid.
It can be said that the space complexity is O(1), as it is constant, no
matter how large the input number may get. 