#!usr/bin/python3
import unittest
from create_sudoku import *


def val_range(test_item):
    c = 0
    for i in test_item:
        if i in range(1, 10):
            c = c + 1
    if c != 9:
        return False


def unique(test_item):
    if len(set(test_item)) == 9:
        return True
    else:
        return False


class Test_to_be_done(unittest.TestCase):
    def __init__(self, test_item):
        self.test_item = test_item
        unique(test_item)
        val_range(test_item)



class test_row_of_sudoku:



class test_col_of_sudoku:
    pass


class test_house():
    pass


class test_sudoku():

    def test_row(self):
        pass

    def test_col(self):
        pass

    def test_house(self):
        pass

    def test_row_one_is_valid(self):
        pass

    def test_row_two_is_valid(self):
        pass

    def test_row_three_is_valid(self):
        pass

    def test_row_four_is_valid(self):
        pass

    def test_row_five_is_valid(self):
        pass

    def test_row_six_is_valid(self):
        pass

    def test_row_seven_is_valid(self):
        pass

    def test_row_eight_is_valid(self):
        pass

    def test_row_nine_is_valid(self):
        pass
