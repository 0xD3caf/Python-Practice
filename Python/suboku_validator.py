def done_or_not(puzzle): #board[i][j]
    '''
    https://www.codewars.com/kata/53db96041f1a7d32dc0004d2
    
    validates if sudoku is correctly finished
    checks all squares, cols, and rows for completeness, if done returns True, if error found or not complete, returns false.
    '''
    rtn_string = "Try again!"
    for tile in [[1,1],[1,4],[1,7],[4,1],[4,4],[4,7],[7,1],[7,4],[7,7]]:
        tile_val_list = []
        for i in range(-1, 2):
            for j in range(-1,2):
                tile_val_list.append(puzzle[tile[0]-i][tile[1]-j])
        if len(set(tile_val_list)) != 9 or 0 in tile_val_list:
            return rtn_string
    for i in range(9):
        if len(set(puzzle[i])) != 9 or 0 in puzzle[i]:
            return rtn_string
        col_list = []
        for j in range(9):
            col_list.append(puzzle[j][i])
        if len(set(col_list)) != 9 or 0 in col_list:
            return rtn_string
    return "Finished!"