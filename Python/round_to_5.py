def round_to_next5(n):
    '''
    https://www.codewars.com/kata/55d1d6d5955ec6365400006d
    
    given integer n, round to nearest multiple of 5
    '''
    test = n%5
    if test != 0:
        return n + (5 - n%5)
    else:
        return n