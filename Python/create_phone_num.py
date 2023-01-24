def create_phone_number(n):
    '''
    https://www.codewars.com/users/macandcheese/completed_solutions
    
    given arr n of integers, return string in form of a phone number
    '''
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)