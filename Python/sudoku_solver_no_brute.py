'''
https://www.codewars.com/kata/5296bc77afba8baa690002d7

solves 9x9 sudoku using human similiar logic instead instead of brute force
starting puzzle will always be solveable
'''
class grid_9():
    def __init__(self):
        self.valid_nums = []
        self.tiles = []

    def add_valid_num(self, num):
        self.valid_nums.append(num)
    
    def remove_valid_num(self, num):
        self.valid_nums.remove(num)

    def get_valid_num(self):
        return self.valid_nums

    def set_valid_tiles(self, tile):
        self.tiles.append(tile)

    def remove_valid_tile(self, tile):
        self.tiles.remove(tile)
    
    def get_valid_tile(self):
        return self.tiles

    def view_grid(self):
        print("Free Tiles are: ", end ="")
        for tile in self.tiles:
            print(tile, end=" ")
        print("\nValid Nums are: {}".format(str(self.valid_nums)))

puzzle1 = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

puzzle2 =[[0,0,0,3,0,2,0,0,1],
          [2,0,3,6,0,0,0,5,9],
          [0,0,0,0,0,0,8,3,0],
          [8,4,0,0,0,0,9,1,0],
          [0,3,6,7,4,1,2,8,0],
          [0,5,7,0,2,0,0,4,3],
          [0,9,4,0,0,0,0,0,0],
          [7,8,0,0,0,9,5,0,6],
          [6,0,0,8,0,7,0,0,0]]

solved_puzzle =[[7,3,5,6,1,4,8,9,2],
          [8,4,2,9,7,3,5,6,1],
          [9,6,1,2,8,5,3,7,4],
          [2,8,6,3,4,9,1,5,7],
          [4,1,3,8,5,7,9,2,6],
          [5,7,9,1,2,6,4,3,8],
          [1,5,7,4,9,2,6,8,3],
          [6,9,4,7,3,8,2,1,5],
          [3,2,8,5,6,1,7,4,9]]


def check_grid(puzzle, grid, num):
    #takes a grid, and num and checks if there is a valid space in that grid that takes that num
    valid_cell = []
    free_spaces = grid.get_valid_tile()
    for space in free_spaces:
        if check_row(puzzle, space[0], num) and check_col(puzzle, space[1], num):
            valid_cell.append(space)
    if len(valid_cell) == 1:
        return valid_cell
    else:
        return []

def check_col(puzzle, col, num):
    #takes a num and column and checks if number exists at any point in that column, returns False if exists, True if not.
    col_list = []
    for x in range(9):
        col_list.append(puzzle[x][col])
    if num in col_list:
        return False
    else:
        return True

def check_row(puzzle, row, num):
    if num in puzzle[row]:
        return False
    else:
        return True

def get_base(cell):
    #takes single cell and returns the base for dict access
    return str(cell[0]) + str(cell[1])

def update_dicts():
    #potential function to update all dicts given a cell and num
    pass

def fill_cell(puzzle, grid_item, cell, num):
    #takes num and location and fills cell with valid num, should also edit grid item to remove both free cell and number from valid list
    puzzle[cell[0]][cell[1]] = num
    grid_item.remove_valid_tile(cell)
    grid_item.remove_valid_num(num)
    if len(grid_item.get_valid_tile()) == 0:
        return True
    return False

def complete_puzzle_check(puzzle):
    #checks all squares, cols, and rows for completeness, if done returns True, if error found or not complete, returns false.
    for tile in [[1,1],[1,4],[1,7],[4,1],[4,4],[4,7],[7,1],[7,4],[7,7]]:
        tile_val_list = []
        for i in range(-1, 2):
            for j in range(-1,2):
                tile_val_list.append(puzzle[tile[0]-i][tile[1]-j])
        if len(set(tile_val_list)) != 9 or 0 in tile_val_list:
            return False
    for i in range(9):
        if len(set(puzzle[i])) != 9 or 0 in puzzle[i]:
            return False
        col_list = []
        for j in range(9):
            col_list.append(puzzle[j][i])
        if len(set(col_list)) != 9 or 0 in col_list:
            return False
    return True


def make_dicts(puzzle, grid_dict):
    #startup function, creates all grids, fills with empty spaces and numbers needed, then adds to dict using str version of coords as key
    #ex [1,7 -> "17"``
    base_tiles = [[1,1],[1,4],[1,7],[4,1],[4,4],[4,7],[7,1],[7,4],[7,7]]
    for tile in base_tiles:
        dict_key = str(tile[0]) + str(tile[1])
        grid_item = grid_9()
        used_nums = []
        for i in range(-1, 2):
            for j in range(-1,2):
                tile_value = puzzle[tile[0]-i][tile[1]-j]
                if tile_value == 0:
                    grid_item.set_valid_tiles([tile[0]-i, tile[1]-j])
                else:
                    used_nums.append(tile_value)
        for num in [1,2,3,4,5,6,7,8,9]:
            if num not in used_nums:
                grid_item.add_valid_num(num)
        grid_dict[dict_key] = grid_item
    for row in puzzle:
        pass


def sudoku(puzzle):
    grid_dict  = {}
    make_dicts(puzzle, grid_dict)
    done = False
    while done == False:
        for grid in grid_dict.values():
            for num in grid.get_valid_num():
                possible_cell = check_grid(puzzle, grid, num)
                if possible_cell != []:
                    fill_cell(puzzle, grid, possible_cell[0], num)
        done = complete_puzzle_check(puzzle)
    else:
        return puzzle

def view_puzzle(puzzle):
    #prints the puzzle in human readable form
    for row in puzzle:
        print(row)