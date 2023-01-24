def solution(number):
    '''
    https://www.codewars.com/kata/514b92a657cdc65150000006
    
    given int number, return all multiples of 3 or 5 that are > number
    '''
    total = 0
    for x in range(number):
        if x > 0 and x % 5 == 0 or x % 3 == 0:
            total += x
    return total