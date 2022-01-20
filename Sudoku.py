def find_next_empty(puzzle):            # finds the empty square(row,col) on the puzzle 
    for r in range(9):
        for c in range(9): # range(9) is 0, 1, 2, ... 8
            if puzzle[r][c] == -1:
                return r, c

    return None, None       # if all square's filled up

def is_valid(puzzle, guess, row, col):      # if a guess is correct to fill itarated square

    # if the guess is already in the row
    row_vals = puzzle[row]          #stores the filled row values
    if guess in row_vals:
        return False 

    # if the guess is already in the column
    col_vals = []
    for i in range(9):
        col_vals.append(puzzle[i][col])
    
    if guess in col_vals:
        return False

    # # if the guess is already in a box
    row_start = (row // 3) * 3          #finds the starting square of a box
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):       #iterates each cells of 3*3 boxes
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True

def solve_sudoku(puzzle):
    
    row, col = find_next_empty(puzzle)

    if row is None:  # this is true if our find_next_empty function returns None, None
        return True 
    
    for guess in range(1, 10): # guessing a number to fit in
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True
        
        # if the guess is not valid
        puzzle[row][col] = -1

    # step 6: if none of the numbers that we try work, then this puzzle is UNSOLVABLE!!
    return False

from pprint import pprint

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    
    pprint(example_board)
