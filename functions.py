"""This module contains all the functions necessary to create, split and test a sudoku"""

import pandas as pd
import numpy as np


def return_solutions(filename, col, number_of_items):
    """return_solutions() will read the user specified csv filename and column and return a list of items
    from that column """
    data = pd.read_csv(filename)  # reading the csv file using pandas
    ls = data[col].tolist()  # converting the whole df to a list
    new_ls = []
    for i in range(number_of_items):
        new_ls.append(ls[i])  # appending a new list with the required number of elements
    return new_ls


def create_nparray(strr):
    """create_nparray from list of strings provided by return_solutions"""
    wd = []
    for ch in strr:
        wd.append(ch)  # converting the string to a list
    arr = []
    counter = 0
    for i in range(9):
        sub = []
        for j in range(9):
            sub.append(wd[counter])
            counter += 1
        arr.append(sub)  # creating a 9x9 array
    return np.array(arr).astype(np.int32)  # type converting the array to an 2d np array with int32 type


def create_list_of_grids():
    """creates a list of sudoku grids to ease use later"""
    ls_grids = []
    #   num = input("How many sudokus do you want to create: ")
    ls = return_solutions("sudoku.csv", "solutions", 10)  # It will return a list of 10 sudoku strings
    for items in ls:
        if pre_check(items):
            n = create_nparray(items)
            ls_grids.append(n)  # apprnding the list with the np arrays
        else:
            print("invalid ")
    return ls_grids


def pre_check(string):
    """simple pre check function to check if all the values in sudoku are digits"""
    return string.isdigit()


def split_into_rows(grid):
    """splitter function to return rows of sudoku"""
    rows = grid[0:, :]
    return rows


def split_into_cols(grid):
    """splitter function to return columns of sudoku"""
    cols = []
    for col in range(9):
        cols.append(grid[:, col])
    return cols


def split_into_subgrids(grid):
    """splitter function to return 3x3 subgrids of sudoku"""
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
    """trial of simple test to make code simpler
    This can be ignored for now as it hold little to no significance"""
    return np.all(np.sort(test_item, axis=-1) == np.arange(1, 10), axis=-1)


def val_range(test_item):
    """testing function that check if the values in a test item (row, col or subgrid) are within
    range,i.e 1 to 9"""
    count = 0
    for val in test_item:
        if 1 <= val <= 9:
            count = count + 1
    if count != 9:
        return False


def unique(test_item):
    """Testing function to check if all the values in a test item are unique,
    i.e without duplicates"""
    return len(set(test_item)) == 9
    # conversion to set only hold unique values and if its len is 9 then we
    # know that the valus inside the test item are unique


if __name__ == "__main__":
    ls = create_list_of_grids()
    for item in ls:  # for grids in list of grids
        print(item)
        for i in split_into_rows(item):  # split grid in to rows and check if they are valid
            if val_range(i) and unique(i):
                pass
            else:
                break
        print("Rows checked")  # return a confirmation ensuring all rows are checked
        for i in split_into_cols(item):  # split grid in to columns and check if they are valid
            if val_range(i) and unique(i):
                pass
            else:
                break
        print("Cols checked")
        # return a confirmation ensuring all cols are checked
        for i in split_into_subgrids(item):  # split grid in to 3x3 subgrids and check if they are valid
            if val_range(i) and unique(i):
                pass
            else:
                break
        print("Subgrids checked")  # return a confirmation ensuring all subgrids are checked

        # trying simple approach
        # can be ignored, this was just a new approach to verify sudoku
        for i in split_into_subgrids(item):
            if simple_test(i):
                pass
            else:
                break
        print("Subgrids checked")
