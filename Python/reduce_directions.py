def dirReduc(arr):
    '''
    https://www.codewars.com/kata/550f22f4d758534c1100025a

    given set of directions, remove any redundant directions, ie move NORTH then SOUTH

    start by finding any sets of cancelling directions
    then repeat looking for new cancelling directions, continue
    '''
    removed = True
    while removed == True:
        removed = False
        #if no item removed this will break loop, if we remove an item then we set to true again
        pop_list = []
        for x in range(len(arr)):
            if arr[x:x+2] in [['NORTH', 'SOUTH'],['SOUTH', 'NORTH'],['EAST', 'WEST'],['WEST', 'EAST']]:
                arr.pop(x)
                arr.pop(x)
                removed = True
    return arr
        