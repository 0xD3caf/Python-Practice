def valid_parentheses(string):
    '''
    https://www.codewars.com/kata/52774a314c2333f0a7000688
    
    given string of parenthesis, determine if the order is valid
    ex, "()" == valid,  ")(()))" == invalid
    '''
    total = 0
    for char in string:
        if char == "(":
            total += 1
        if char == ")":
            total -= 1
            if total < 0:
                return False
    return total == 0