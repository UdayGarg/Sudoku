"""module to print sudoku on a proper sudoku board"""
import functions as func


def nice_sudoku(board):
    """ NICE sudoku representation but *NOT MY CODE*"""

    base = 3
    side = base**2

    def expand_line(line):
        return line[0] + line[5:9].join([line[1:5] * (base - 1)] * base) + line[9:13]

    line0 = expand_line("╔═══╤═══╦═══╗")
    line1 = expand_line("║ . │ . ║ . ║")
    line2 = expand_line("╟───┼───╫───╢")
    line3 = expand_line("╠═══╪═══╬═══╣")
    line4 = expand_line("╚═══╧═══╩═══╝")

    symbol = " 1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums = [[""] + [symbol[n] for n in row] for row in board]
    print(line0)
    for r in range(1, side + 1):
        print("".join(n + s for n, s in zip(nums[r - 1], line1.split("."))))
        print([line2, line3, line4][(r % side == 0) + (r % base == 0)])


if __name__ == "__main__":
    ls = func.create_list_of_grids()
    for data in ls:
        print(nice_sudoku(data))
