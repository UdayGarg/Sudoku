import numpy as np

from input_solved_sudoku import *
import access_file
from random import randint

ran = randint(1, 1000)
print(ran)
unsolved_grid = create_nparray(access_file.return_solutions("sudoku.csv", "quizzes", 1)[0])
solved_grid = create_nparray(access_file.return_solutions("sudoku.csv", "solutions", 1)[0])
print(unsolved_grid)
print(solved_grid)

"""
grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 0, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]


def possible(row, column, num):
    global grid
    for i in range(9):
        if grid[row][i] == num:
            return False
    for i in range(9):
        if grid[i][column] == num:
            return False
    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[y0 + i][x0 + j] == num:
                return False
    return True


def solve():
    global grid
    for row in range(0, 9):
        for column in range(0, 9):
            if grid[row][column] == 0:
                for number in range(1, 10):
                    if possible(row, column, number):
                        grid[row][column] = number
                        solve()
                        grid[row][column] = 0
                return
    print(np.matrix(grid))



#   grid = create_nparray(access_file.return_solutions("sudoku.csv", "quizzes", 1)[0])
"""

"""
if __name__ == "__main__":
    ls = access_file.return_solutions("sudoku.csv", "quizzes", 1)
    for items in ls:
        if pre_check(items):
            grid = create_nparray(items)
            solve()
        else:
            print("invalid ")

grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 0, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]
"""


def possible(row, column, number):
    global grid
    for i in range(9):
        if grid[row][i] == number:
            return False

    for i in range(9):
        if grid[i][column] == number:
            return False

    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0 + i][x0 + j] == number:
                return False

    return True


def solve(grid):
    for row in range(0, 9):
        for column in range(0, 9):
            if grid[row][column] == 0:
                for number in range(1, 10):
                    if possible(row, column, number):
                        grid[row][column] = number
                        solve(grid)
                        grid[row][column] = 0

                return np.matrix(grid)


a = solve(unsolved_grid)
print(a)

if np.array_equal(a, solved_grid):
    print("Success")
else:
    print("Fail")
