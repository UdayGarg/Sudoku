#!usr/bin/python3
import unittest
import splitter
import create_sudoku

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


class TestSudoku(unittest.TestCase):
    def test_rows(self):
        """
        to_test = splitter.split_into_rows(create_sudoku.create_list_of_grids()[1])
        row_test = [8, 6, 4, 3, 7, 1, 2, 5, 9]
        """
        self.assertEqual(val_range(to_test), True)
        self.assertEqual(unique(to_test), True)


    def test_columns(self):
        pass

    def test_house(self):
        pass


if __name__ == "__main__":
    unittest.main()

"""
to fail:
    duplicates
    not 81 values
    if input not digit
    
    
    corrupt char
    corrupt len
    corrupt digits
"""
