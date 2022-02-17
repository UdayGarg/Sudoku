#!usr/bin/python3
import unittest


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
        row_test = [8, 6, 4, 3, 7, 1, 2, 5, 9]
        self.assertEqual(val_range(row_test), True)
        self.assertEqual(unique(row_test), True)

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
