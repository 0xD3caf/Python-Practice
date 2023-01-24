numCheck = [1,2,3,4,5,6,7,8,9]
def valid_solution(board):
    '''
    https://www.codewars.com/kata/529bf0e9bdf7657179000008

    given arr board, check if sudoku answer is valid
    '''
    status = True
    statusCheck = []
    rowDict = {}
    columnDict = {}
    boxDict = {}
    createDicts(board, columnDict, rowDict, boxDict)
    statusCheck.append(checkRow(rowDict))
    statusCheck.append(checkCol(columnDict))
    statusCheck.append(checkBox(boxDict))
    if statusCheck != [True, True, True]:
        status = False
    return status
    
def createDicts(board, columnDict, rowDict, boxDict,):
    for num in range(len(board)):
        currRow = "row" + str(num)
        currColumn = "col" + str(num)
                
        rowDict[currRow] = board[num]

        columnDict[currColumn] = [board[0][num],board[1][num],board[2][num],board[3][num],board[4][num],board[5][num],board[6][num],board[7][num],board[8][num]]
        if num % 3 == 0:
            currBox1 = "box" + str(num)
            currBox2 = "box" + (str(num + 1))
            currBox3 = "box" + (str(num + 2))
            boxDict[currBox1] = [board[num][0], board[num][1], board[num][2],board[num+1][0], board[num+1][1], board[num+1][2], board[num+2][0], board[num+2][1], board[num+2][2]]
            boxDict[currBox2] = [board[num][3], board[num][4], board[num][5],board[num+1][3], board[num+1][4], board[num+1][5], board[num+2][3], board[num+2][4], board[num+2][5]]
            boxDict[currBox3] = [board[num][6], board[num][7], board[num][8],board[num+1][6], board[num+1][7], board[num+1][8], board[num+2][6], board[num+2][7], board[num+2][8]]    
    return
def checkRow(rowDict):
    for val in rowDict.values():
        if 0 in val:
            return False
        for num in numCheck:
            if num not in val:
                return False
    return True

def checkBox(boxDict):
    for val in boxDict.values():
        for num in numCheck:
            if num not in val:
                return False
    return True
def checkCol(columnDict):
    for val in columnDict.values():
        for num in numCheck:
            if num not in val:
                return False
    return True
    