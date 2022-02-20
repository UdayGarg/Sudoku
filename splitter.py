import access_file
from create_sudoku import create_nparray
import skimage

"""
def split_sudoku(grid):
    print("grid")
    print(grid)
    print('\n')
    print("Rows: \n")
    for rows in grid:
        print(rows)
    print('\n')
    print("Cols: \n")
    for col in range(9):
        print((grid[:, col]))
    print('\n')
    print("House: \n")
    subgrids = skimage.util.view_as_blocks(grid, (3, 3)).reshape(3, 3, -1)  # help taken
    print(subgrids)


ls_size = 100
c = 0  # just for final check
ls = access_file.return_solutions("sudoku.csv", "solutions", ls_size)  # create a list of serialized solutions from
# the sudoku file
print(ls)
print(random.sample(ls, 2))
rand_ls = random.sample(ls, 2)
for item in rand_ls:
    grid = create_nparray(item)  # it takes the strr input and converts it to nparray and split it to rows
    # and columns
    split_sudoku(grid)
    c += 1

print(c)
"""
"""def init_sudoku():
    # n = number of sudokus
    n = 10
    ls = access_file.return_solutions("sudoku.csv", "solutions", n)
    for item in ls:
        grid = create_nparray(item)
        return grid
"""


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


if __name__ == "__main__":
    ls_size = 10
    ls = access_file.return_solutions("sudoku.csv", "solutions", ls_size)

    """for item in ls:
        grid = create_nparray(item)
        print(split_into_subgrids(grid))
        print(split_into_cols(grid))
        print(split_into_rows(grid))"""

