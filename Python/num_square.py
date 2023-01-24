def square_digits(num):
    #https://www.codewars.com/users/macandcheese/completed_solutions
    #returns num squared
    rtrStr = ""
    for digit in str(num):
        rtrStr += (str(int(digit)*int(digit)))
    return int(rtrStr)