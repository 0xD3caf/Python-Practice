def validate_battlefield(field):
    '''
    https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7
    
    given field N (size 10x10), checks if N is a valid battleship configuration
    requirements:
        1. Ships -- EXACTLY 
            1 Battleship (1x4)
            2 Cruisers (1x3)
            3 Destroyers (1x2)
            4 submarines (1x1)
    
        2. all ships MUST be straight lines
        3. No ships can overlap OR  be in contact, indlcuding diagonally
    '''
    shipDict = {4:1, 3:2, 2:3, 1:4}
    CoordList = [[[i,j] for j in range(10)] for i in range(10)]
    for row in CoordList:
        for item in row:
            if field[item[0]][item[1]] == 1:
                test = checkAdjacent(field,[item[0],item[1]], shipDict)
                if not test:
                    displayShips(field)
                    return False
    for row in CoordList:
        for item in row:
            if field[item[0]][item[1]] == 1:
                test = checkShips(field, [item[0],item[1]], shipDict)
                if not test:
                    displayShips(field)
                    return False
    #add call to Checkships HERE
        #if retrusn false, return false
    displayShips(field)
    print(shipDict)
    for item in shipDict.values():
        if item != 0:
            return False
    return True

def checkAdjacent(field, location, shipDict): #passes location as 2 item list
    # only needs to check if diagonal touches
    # any ships touching, or mishaped will always create a diagonal
    count = 0
    diag_check = False
    check_list = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    for item in check_list:
        yCoord = location[0] + item[0]
        if yCoord < 0 or yCoord > 9:
            continue
        xCoord = location[1] + item[1]
        if xCoord < 0 or xCoord > 9: 
            continue
        if field[yCoord][xCoord] == 1:
            count += 1
            if 0 not in item:
                diag_check = True
    if count > 2 or diag_check:
        return False
    elif count == 0:
        shipDict.update({1:shipDict.get(1) - 1})
        field[location[0]][location[1]] = 2
    return True

def checkShips(field, start_point, shipDict):
    count = 0
    #Directions are [UP, DOWN / LEFT, RIGHT]
    xDirection = [False, False]
    yDirection = [False, False]
    check_list = [[0,-1],[0,1],[-1,0],[1,0]]
    for item in check_list:
        yCoord = start_point[0] + item[0]
        if yCoord < 0 or yCoord > 9:
            continue
        xCoord = start_point[1] + item[1]
        if xCoord < 0 or xCoord > 9:
            continue
        if field[yCoord][xCoord] == 1:
            if item[0] == 0:
                if item[1] == -1:
                    xDirection[0] = True
                else:
                    xDirection[1] = True
            else:
                if item[0] == -1:
                    yDirection[0] = True
                else:
                    yDirection[1] = True    
    if yDirection[0]:
        return traverseY(field, -1, start_point,shipDict)
    elif yDirection[1]:
        return traverseY(field, 1, start_point,shipDict)
    elif xDirection[0]:
        return traverseX(field, -1, start_point,shipDict)
    elif xDirection[1]:
        return traverseX(field, 1, start_point,shipDict)
    return True

def traverseX(field, direction, start, shipDict):
    # moves across x Direction ship
    cellCount = 1
    shipHead = []
    done = False
    next = 1
    #position first
    #need to add in the orig direction to tile mod
    while next == 1:
        if start[1] + (cellCount * direction) < 0 or start[1] + (cellCount * direction) > 9:
            next = 0
        elif field[start[0]][start[1] + (cellCount * direction)] != 1:
            next = 0
        else:
            cellCount += 1
    else:   #saves vars at the end
        shipHead.append(start[0])
        shipHead.append(start[1] + ((cellCount-1) * direction))

    #then count and change
    direction = direction * -1
    cellCount = 1
    while not done:
        if shipHead[1] + (cellCount * direction) < 0 or shipHead[1] + (cellCount * direction) > 9:
            done = True
        elif field[shipHead[0]][shipHead[1] + (cellCount * direction)] != 1:
            done = True
        else:
            field[shipHead[0]][shipHead[1] + (cellCount * direction)] = 2
            cellCount += 1
            #change current value to 2
    if cellCount > 4:
        print("bad ship found: Too Long")
        return False
    else:
        dict_mod = shipDict.get(cellCount) - 1
        shipDict.update({cellCount:dict_mod})    
    for item in shipDict.values():
        if item < 0:            
            print("bad ship found, too many of a ship")
            return False
    return True

def traverseY(field, direction, start, shipDict):
    #moves across y direction ship
    cellCount = 1
    shipHead = []
    done = False
    next = 1
    #position first
    #need to add in the orig direction to tile mod
    while next == 1:
        if start[0] + (cellCount * direction) < 0 or start[0] + (cellCount * direction) > 9:
            next = 0
        elif field[start[0]  + (cellCount * direction)][start[1]] != 1:
            next = 0
        else:
            cellCount += 1
    else:   #saves vars at the end
        shipHead.append(start[0] + ((cellCount-1) * direction))
        shipHead.append(start[1])
        
    #then count and change
    direction = direction * -1
    cellCount = 1
    while not done:
        if shipHead[0] + (cellCount * direction) < 0 or shipHead[0] + (cellCount * direction) > 9:
            done = True
        elif field[shipHead[0] + (cellCount * direction)][shipHead[1]] != 1:
            done = True
        else:
            field[shipHead[0]+ (cellCount * direction)][shipHead[1]] = 2
            cellCount += 1
            #change current value to 2
    if cellCount > 4:
        print("bad ship found: Too Long")
        return False
    else:
        dict_mod = shipDict.get(cellCount) - 1
        shipDict.update({cellCount:dict_mod})
    for item in shipDict.values():
        if item < 0:
            print("bad ship found, too many of ship type")
            return False
    return True

def displayShips(field):
    for line in field:
        print(line)
    print()