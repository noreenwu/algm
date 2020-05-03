def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    next_0 = 0
    next_2 = len(input_list) - 1

    idx = 0

    while idx <= next_2:
        if input_list[idx] == 0:
            # we've encountered a 0: move it to where the zero's belong (based on next_0)
            input_list[idx] = input_list[next_0]
            input_list[next_0] = 0
            next_0 += 1
            idx += 1
        elif input_list[idx] == 2:
            # we've encountered a 2: move it to where the 2's are (based on next_2)
            input_list[idx] = input_list[next_2]
            input_list[next_2] = 2
            next_2 -= 1
        else:
            idx += 1
    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


# sorted_array = sort_012([0, 0, 2, 1, 1, 0])
# print(sorted_array)
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
