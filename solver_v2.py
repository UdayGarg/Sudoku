from input_solved_sudoku import *
import access_file


def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False

    for x in range(9):
        if grid[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True


def Suduko(grid, row, col):
    if row == 8 and col == 9:
        return True
    if col == 9:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Suduko(grid, row, col + 1)
    for num in range(1, 10):

        if solve(grid, row, col, num):

            grid[row][col] = num
            if Suduko(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False


'''0 means the cells where no value is assigned'''
"""
grid = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
        [0, 1, 0, 0, 0, 4, 0, 0, 0],
        [4, 0, 7, 0, 0, 0, 2, 0, 8],
        [0, 0, 5, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 8, 1, 0, 0],
        [0, 4, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 3, 6, 0, 0, 7, 2],
        [0, 7, 0, 0, 0, 0, 0, 0, 3],
        [9, 0, 3, 0, 0, 0, 6, 0, 4]]"""

unsolved_grid = create_nparray(access_file.return_solutions("sudoku.csv", "quizzes", 1)[0])
actual = create_nparray(access_file.return_solutions("sudoku.csv", "solutions", 1)[0])
new_actual = actual.astype(np.int32).tolist()
new_actual1 = np.array(new_actual)
grid = unsolved_grid.astype(np.int32).tolist()

if Suduko(grid, 0, 0):
    solved_grid = np.array(grid)
    print(type(solved_grid))
    print(f"Actual :\n {new_actual1} \n Solved :\n {solved_grid}")
    print(type(new_actual1))
    print(type(solved_grid))

else:
    print("Solution does not exist:(")

comparison = new_actual1 == solved_grid
equal_arrays = comparison.all()
if equal_arrays:
    print("Viola! code works")
else:
    print("Fail")
