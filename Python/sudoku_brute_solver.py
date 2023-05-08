#https://www.codewars.com/kata/55171d87236c880cea0004c6/
'''
Description:

This kata is a harder version of http://www.codewars.com/kata/sudoku-solver/python made by @pineappleclock

Write a function that will solve a 9x9 Sudoku puzzle. The function will take one argument consisting of the 2D puzzle array, with the value 0 representing an unknown square.

The Sudokus tested against your function will be "insane" and can have multiple solutions. The solution only need to give one valid solution in the case of the multiple solution sodoku.

It might require some sort of brute force.

For Sudoku rules, see the Wikipedia : http://www.wikiwand.com/en/Sudoku

Used puzzle from : http://www.extremesudoku.info/sudoku.html
'''
def solve(board):
    #Could be a little more efficient by checking for spaces solveable with traditional sudoku logic
    head = None
    prev = None
    for i in range(9):                                      #creates node item for each tile in sudoku board
        for j in range(9):
            if board[i][j] == 0:
                sudoku_tile = Node(board[i][j], [i,j])
                if prev == None:                            #if first time running, set head and save current tile
                    head = sudoku_tile
                    prev = sudoku_tile
                else:
                    sudoku_tile.prev = prev                 #set new tile previous to saved tile
                    prev.next = sudoku_tile                 #set saved tile next to new tile
                    prev = sudoku_tile                      #save new tile as prev for next loop
    Done = False
    curr_node = head

    while Done == False:
        if curr_node.next == None:          #backup escape for errors
            Done = True
        next_val = 0
        board_space = curr_node.board_space             #set working tile
        for i in range(curr_node.value + 1, 10):        #loop from current tile value to max tile value, default starts at 0
            if i in board[board_space[0]]:                  #check if current number already in row
                continue
            if i in [x[board_space[1]] for x in board]:     #check if current number already in column
                continue
            row_start = int(board_space[0] // 3) * 3        #calc nearest multiple of 3 below for row, used as offset to access 3x3 box of values
            col_start = int(board_space[1] // 3) * 3        #same as above for column
            if i in [board[row_start][col_start], board[row_start][col_start +1], board[row_start][col_start +2],board[row_start +1][col_start], board[row_start +1][col_start +1], board[row_start +1][col_start +2],board[row_start +2][col_start], board[row_start +2][col_start +1], board[row_start +2][col_start +2]]:
                continue
            next_val = i
            break
        if next_val != 0:                                       #checks if valid number for tile was found
            curr_node.value = next_val                              #set node item value to new value
            board[board_space[0]][board_space[1]] = next_val        #set board space array value to new value
            curr_node = curr_node.next                              #move to next node
        else:                                       #no valid number found
            curr_node.value = 0                         #reset tile value to 0
            board[board_space[0]][board_space[1]] = 0   #reset board array space value to 0
            curr_node = curr_node.prev                  #move to previous node
    return board

class Node:
    #node class to allow forward and backward movement through sudoku values
    def __init__(self, value, board_space):
        self.prev = None
        self.next = None
        self.value = value                         
        self.board_space = board_space          #x,y coords for accessing item in board array