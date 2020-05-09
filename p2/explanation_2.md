# Find number in a rotated sorted array

Again, it is tempting to step through the array looking for the value
and returning it once there is a match, or return -1 when it becomes
clear that the value has been passed. This method would take O(N) only
in the worst case, when the value searched for is in the very last position
of the array.

Binary search makes it possible to achieve O(log N) efficiency, an improvement
over O(N). But the problem must be divided into 2 steps: 1) find the "pivot" or the
last element in the array prior to rotation and 2) binary search either
the subarray to the left or to the right of the pivot. This may be 
determined by comparing the searched for element with the very first
element of the array. If the number is larger than or equal to the first element, the
left side of the pivot needs to be searched; otherwise the right
side. This 2nd stage binary search also takes log N time, so 2 log N
processes, or essentially O(log N) together.

