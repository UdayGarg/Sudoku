#!/usr/bin/python3
import numpy as np


def create_nparray(strr):
    wd = []
    for ch in strr:
        wd.append(ch)
    print(len(wd))
    arr = []
    counter = 0
    for i in range(9):
        sub = []
        for j in range(9):
            sub.append(wd[counter])
            counter += 1
        arr.append(sub)
    return np.array(arr)

def pre_check(string):
    return string.isdigit()


solved = "346179258187523964529648371965832417472916835813754629798261543631485792254397186"
if pre_check(solved):
    n = create_nparray(solved)
    print(n)
else: print("invalid ")
