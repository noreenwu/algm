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

    if number == 0 or number == 1:
        return display_answer(number)
        
    lower = 1
    mid = number // 2
    upper = number

    i = 0
    while lower <= upper and i < 10:
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