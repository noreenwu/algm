def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    pass

def find_pivot(input_list, low, high):
    print("pivot high {}".format(input_list[high]))

    mid = (low + high) // 2
    


    i = 0
    while low <= high and i < 10:
        if input_list[mid] > input_list[mid+1]:
            print("got the pivot: {}".format(input_list[mid]))
            return mid        

        # did not find pivot yet: search left or right side of array chunk
        if input_list[mid] < input_list[high]:
            # then we must be on the right side of the pivot: check left
            print("checking left")
            high = mid
            mid = (low + high) // 2
        else:
            # check right
            print("checking right")
            low = mid + 1
            mid = (low + high) // 2

        i += 1


def bin_search_det(input_list, low, high, number):
    pass


def bin_search(input_list, number):
    p = find_pivot(ary, 0, len(ary)-1)
    print("pivot index was {}".format(p))    

    ## once the pivot is identified, determine whether to search
    ## to the left of the pivot or to the right of it
    ## if target is > item at 0th location, then search left side 
    ## (delimited by pivot) 0..pivot
    ## but if target is < item at 0th location, then search
    ## from pivot+1st location through end of array pivot+1..n-1

    if number > input_list[0]:
        bin_search_det(input_list, 0, p, number)

    else:
        bin_search_det(input_list, p+1, len(input_list)-1, number)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


ary = [6, 7, 8, 9, 10, 1, 2, 3, 4]
ary2 = [8, 1, 2, 3, 4, 5, 6, 7]

bin_search(ary, 6)
# p = find_pivot(ary2, 0, len(ary2)-1)
# print("pivot index was {}".format(p))



# test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
# test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
# test_function([[6, 7, 8, 1, 2, 3, 4], 8])
# test_function([[6, 7, 8, 1, 2, 3, 4], 1])
# test_function([[6, 7, 8, 1, 2, 3, 4], 10])
