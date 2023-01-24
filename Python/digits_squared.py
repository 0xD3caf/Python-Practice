def square_digits(num):
    '''
    https://www.codewars.com/users/macandcheese/completed_solutions
    square each digit of num and return string of all digits squared
    ex.
    9119 == 811181: 9^2(81) 1^2(1) 1^2(1) 9^2(81)
    '''

    rtrStr = ""
    for digit in str(num):
        rtrStr += (str(int(digit)*int(digit)))
    return int(rtrStr)