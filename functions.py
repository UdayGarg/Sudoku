import pandas as pd
import numpy as np
import skimage


def return_solutions(filename, col, n):
    data = pd.read_csv(filename)
    ls = data[col].tolist()
    new_ls = []
    for i in range(n):
        new_ls.append(ls[i])
    return new_ls


def create_nparray(strr):
    wd = []
    for ch in strr:
        wd.append(ch)
    arr = []
    counter = 0
    for i in range(9):
        sub = []
        for j in range(9):
            sub.append(wd[counter])
            counter += 1
        arr.append(sub)
    return np.array(arr).astype(np.int32)


def create_list_of_grids():
    ls_grids = []
    #   num = input("How many sudokus do you want to create: ")
    ls = return_solutions("sudoku.csv", "solutions", 10)
    for items in ls:
        if pre_check(items):
            n = create_nparray(items)
            ls_grids.append(n)
        else:
            print("invalid ")
    return ls_grids


def pre_check(string):
    return string.isdigit()


def split_into_rows(grid):
    rows = []
    for row in grid:
        rows.append(row)
    return rows


def split_into_cols(grid):
    cols = []
    for col in range(9):
        cols.append(grid[:, col])
    return cols


def split_into_subgrids(grid):
    subgrids = skimage.util.view_as_blocks(grid, (3, 3)).reshape(3, 3, -1)
    return subgrids