def snail(snail_map):
    '''
    https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

    given arr of NxN, return elements arranged from outmost to innermost traveling clockwise
    array = 
    [[1,2,3],
     [8,9,4],
     [7,6,5]]
    snail(array) #=> [1,2,3,4,5,6,7,8,9]
    '''
    
    snail_trail = []
    curr_len = len(snail_map)
    if [] in snail_map:
        return []
    while curr_len != 0:
        if curr_len == 1:
            for mylst in snail_map:
                if len(mylst) != 0:
                    snail_trail.append(mylst[0])
                    curr_len -= 1
        else:            
                #find only object and append
            for x in range(curr_len):                            #removes the top row
                snail_trail.append(snail_map[0].pop(0))
            
            for x in range(1, curr_len -1):                        #removes the right side (middle tiles only)
                snail_trail.append(snail_map[x].pop())        
            
            for x in range(curr_len):                            #removes the bottom row
                snail_trail.append(snail_map[curr_len -1].pop())
                
            for x in range(curr_len -2, 0, -1):                    #removes the left side(middle tiles only)
                snail_trail.append(snail_map[x].pop(0))
            snail_map.pop(0)
            snail_map.pop()
            curr_len -= 2
        print(snail_trail)
        #for n in range(1, curr_len + 2):
         #   snail_trail.append(snail_map[curr_len].pop())
            
    #starts at 3, then 3x2, 2x2, 1x2
    return snail_trail
