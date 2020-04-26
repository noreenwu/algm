def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == 0 or number == 1:
        return number

        
    lower = 1
    mid = number // 2
    upper = number

    i = 0
    while lower <= upper and i < 10:
        print("trying {} with lower {} and upper {}".format(mid, lower, upper))
        if mid * mid == number:
            return mid

        if mid * mid  < number:
            print("\twe are under")
            lower = mid+1
        if mid * mid > number: 
            print("\twe are over: look in lower half")
            upper = mid-1

        mid = (upper + lower) // 2
        print("\tnew mid is {} in range {} to {}".format(mid, lower, upper))
        i += 1


    print("lower {} mid {} upper {}".format(lower, mid, upper))
    return mid

print ("Pass" if  (6 == sqrt(36)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (25 == sqrt(625)) else "Fail")