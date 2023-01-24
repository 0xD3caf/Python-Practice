def narcissistic( value ):
    '''
    https://www.codewars.com/kata/5287e858c6b5a9678200083c
    
    given val, check if value is a narcissistic number (sum of all digits raised to power len(val) == to number)
    '''
    import math
    check = False
    total = 0
    lencheck = len(str(value))
    for int in range(1, lencheck + 1):
        digit = get_digit(value, int - 1)
        total += math.pow(digit, lencheck)
    print(total)
    if total == value:
        check = True
    return check
    
def get_digit(number, n):
    return number // 10**n % 10
