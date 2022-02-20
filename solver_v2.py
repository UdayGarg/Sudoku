#from input_solved_sudoku import *
import access_file
import time
import numpy as np

from create_sudoku import create_nparray


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

if __name__ == "__main__":
    start = time.time()
    unsolved_grid = create_nparray(access_file.return_solutions("sudoku.csv", "quizzes", 1)[0])
    actual_grid = create_nparray(access_file.return_solutions("sudoku.csv", "solutions", 1)[0])
    grid = unsolved_grid.tolist()
    print(unsolved_grid)
    print(actual_grid)
    """
    grid = [[0, 0, 0, 0, 0, 0, 0, 7, 0],
            [0, 0, 0, 7, 0, 0, 3, 0, 9],
            [0, 0, 0, 0, 0, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 7],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 6, 0]]
    """
    solved_grid = 0
    if Suduko(grid, 0, 0):
        solved_grid = np.array(grid)
        print(solved_grid)
    else:
        print("Solution does not exist:(")

    comparison = actual_grid == solved_grid
    equal_arrays = comparison.all()
    if equal_arrays:
        print("Viola! code works (verification successful)")
    else:
        print("Fail")
    print(f"time taken = {time.time() - start:.4}s")
