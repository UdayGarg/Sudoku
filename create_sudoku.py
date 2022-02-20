#!/usr/bin/python3
import numpy as np
import access_file


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
    ls = access_file.return_solutions("sudoku.csv", "solutions", 10)
    for items in ls:
        if pre_check(items):
            n = create_nparray(items)
            ls_grids.append(n)
        else:
            print("invalid ")
    return ls_grids


def pre_check(string):
    return string.isdigit()


"""solved = "346179258187523964529648371965832417472916835813754629798261543631485792254397186"
if pre_check(solved):
    n = create_nparray(solved)
    print(n)
else:
    print("invalid ")"""

if __name__ == "__main__":
    """
    ls_grids = []
    num = input("How many sudokus do you want to create: ")
    ls = access_file.return_solutions("sudoku.csv", "solutions", int(num))
    for items in ls:
        if pre_check(items):
            n = create_nparray(items)
            ls_grids.append(n)
        else:
            print("invalid ")
    print(ls_grids[2])"""
    l = create_list_of_grids()
    for i in l:
        print(i)

