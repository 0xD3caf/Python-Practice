from itertools import permutations as perms
def permutations(string):
    '''
    https://www.codewars.com/kata/5254ca2719453dcc0b00027d

    create all permutations of a non empty string without duplicates
    '''
    return ["".join(x) for x in set(perms(string))]