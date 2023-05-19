puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
def print_sudoku(puzzle):
    horizontal_line = "+-------+-------+-------+"

    for i in range(9):
        if i % 3 == 0:
            print(horizontal_line)

        for j in range(9):
            if j % 3 == 0:
                print("|", end=" ")

            if puzzle[i][j] == -1:
                print(" ", end=" ")
            else:
                print(puzzle[i][j], end=" ")

            if j == 8:
                print("|")

    print(horizontal_line)
def next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if(puzzle[r][c]==0):
                return r, c
    return None, None
def is_valid(puzzle,guess,row,col):
    row_vals=puzzle[row]
    if(guess in row_vals):
        return False
    col_vals=[puzzle[i][col] for i in range(9)]
    if(guess in col_vals):
        return False
    box_row=(row//3)*3
    box_col=(col//3)*3
    for i in range(box_row,box_row+3):
        for j in range(box_col,box_col+3):
            if(puzzle[i][j]==guess):
                return False
    return True
def sudoku_solver(puzzle):

    row, col=next_empty(puzzle)
    
    if(row==None):
        return True

    for guess in range(1,10):
        if(is_valid(puzzle,guess,row,col)):
            puzzle[row][col]=guess
            if(sudoku_solver(puzzle)):
                return True
        puzzle[row][col]=0
    return False

print(sudoku_solver(puzzle))
print_sudoku(puzzle)
