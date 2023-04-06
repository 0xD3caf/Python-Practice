def is_valid_walk(walk):
    '''
    https://www.codewars.com/kata/54da539698b8a2ad76000228
    
    given arr walk, determine if arr is a valid walk taking 10 mintues and returning to starting point
    arr is list of "n,s,e,w" each block taking one min to walk
    '''
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')
        #checks if length is equal 10, and both noth + south pair and east + west pair occur same number of times
