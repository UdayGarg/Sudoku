"""The function of this module is to form and print table from array to publish suitable looking SUDOKU
puzzles"""

from tabulate import tabulate
import functions as func


def tabulate_data(item):
    """Function to create tables from array using external module "tabulate" """
    tb = (tabulate(item, tablefmt="fancy_grid"))
    return tb


if __name__ == "__main__":
    ls = func.create_list_of_grids()
    for data in ls:
        print(tabulate_data(data))


