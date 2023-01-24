def is_valid_walk(walk):
    '''
    https://www.codewars.com/kata/54da539698b8a2ad76000228
    
    given arr walk, determine if arr is a valid walk taking 10 mintues and returning to starting point
    arr is list of "n,s,e,w" each block taking one min to walk
    '''
    check = False
    if len(walk) == 10:
        totalN = walk.count("n")
        totalS = walk.count("s")
        totalE = walk.count("e")
        totalW = walk.count("w")
        if totalN == totalS and totalE == totalW:
            check = True
    return check