import pandas as pd
import numpy as np


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
    ls = return_solutions("sudoku.csv", "solutions", 10)  # It will return a list of 10 sudoku strings
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
    rows = grid[0:, :]
    return rows


def split_into_cols(grid):
    cols = []
    for col in range(9):
        cols.append(grid[:, col])
    return cols


def split_into_subgrids(grid):
    subgrids = []
    for box_i in range(3):
        for box_j in range(3):
            subgrid = []
            for i in range(3):
                for j in range(3):
                    subgrid.append(grid[3 * box_i + i][3 * box_j + j])
            subgrids.append(subgrid)
    return np.array(subgrids)


def simple_test(test_item):
    if np.all(np.sort(test_item, axis=-1) == np.arange(1, 10), axis=-1):
        return True
    else:
        return False


def val_range(test_item):
    c = 0
    for i in test_item:
        if 1 <= i <= 9:
            c = c + 1
    if c != 9:
        return False
    else:
        return True


def unique(test_item):
    if len(set(test_item)) == 9:
        return True
    else:
        return False


if __name__ == "__main__":
    ls = create_list_of_grids()
    for item in ls:
        for i in split_into_rows(item):
            print(i)
            if val_range(i) and unique(i):
                pass
            else:
                break
        print("Rows checked")
        for i in split_into_cols(item):
            if val_range(i) and unique(i):
                pass
            else:
                break
        print("Cols checked")
        for i in split_into_subgrids(item):
            if val_range(i) and unique(i):
                pass
            else:
                break
        print("Subgrids checked")

        # trying simple approach
        for i in split_into_subgrids(item):
            if simple_test(i):
                pass
            else:
                break
        print("Subgrids checked")
        """if val_range(i) and unique(i):
                pass
            else:
                break"""



