def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list

    mid = len(input_list) // 2
    left = input_list[:mid]
    right = input_list[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)
    

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    
    sorted_input_list = merge_sort(input_list)
    num1 = ''
    num2 = ''
    for idx, n in enumerate(sorted_input_list):
        if idx % 2 == 0:
        #    print("num1 {}".format(n))
           num1 = str(n) + num1
        else:
        #    print("num 2 {}".format(n))
           num2 = str(n) + num2
    # print ("num1 {} and num2 {}".format(num1, num2))
    res = []
    res.append(int(num1))
    res.append(int(num2))
    return res


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# print(rearrange_digits([7, 8, 9, 5, 1, 2]))
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[2, 6, 1, 5, 3], [631, 52]])
