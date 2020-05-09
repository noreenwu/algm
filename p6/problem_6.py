def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min = ints[0]
    max = ints[0]
    for i in ints[1:]:
        if i < min:
            min = i
        if i > max:
            max = i
    tup = (min, max)
    print("returning {}".format(tup))
    return tup

## Example Test Case of Ten Integers
import random

def test_case(size=10):
    l = [i for i in range(0, size)]  # a list containing 0 - 9
    random.shuffle(l)
    return l


l = test_case()
print(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = test_case()
print(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = test_case()
print(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

size = 5
l = test_case(size)
print(l)
print ("Pass" if ((0, size-1) == get_min_max(l)) else "Fail")

size = 2
l = test_case(size)
print(l)
print ("Pass" if ((0, size-1) == get_min_max(l)) else "Fail")

size = 1
l = test_case(size)
print(l)
print ("Pass" if ((0, size-1) == get_min_max(l)) else "Fail")