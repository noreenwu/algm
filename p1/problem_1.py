def display_answer(num):
    """
    Uniformly display the provided answer and return it
    """

    print("\tAnswer: {}".format(num))
    return num

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    print("Find sqrt of {}:".format(number))

    if number < 0:
        print("the square root of a negative number is not a real number")
        return -1

    if number == 0 or number == 1:
        return display_answer(number)
        

    lower = 1
    mid = number // 2
    upper = number

    i = 0
    while lower <= upper:
        if mid * mid == number:
            return display_answer(mid)

        if mid * mid  < number:
            lower = mid+1
        if mid * mid > number: 
            upper = mid-1

        mid = (upper + lower) // 2
        i += 1


    return display_answer(mid)

print ("Pass\n" if  (6 == sqrt(36)) else "Fail")
print ("Pass\n" if  (0 == sqrt(0)) else "Fail")
print ("Pass\n" if  (4 == sqrt(16)) else "Fail")
print ("Pass\n" if  (1 == sqrt(1)) else "Fail")
print ("Pass\n" if  (5 == sqrt(27)) else "Fail")
print ("Pass\n" if  (25 == sqrt(625)) else "Fail")
print ("Pass\n" if  (-1 == sqrt(-64)) else "Fail")              # not a real number message
print ("Pass\n" if  (50 == sqrt(2500)) else "Fail")
print ("Pass\n" if  (112 == sqrt(12544)) else "Fail")
print ("Pass\n" if  (1122 == sqrt(1258884)) else "Fail")
print ("Pass\n" if  (99999 == sqrt(9999800001)) else "Fail")