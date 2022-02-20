import pandas as pd


def return_solutions(filename, col, n):
    data = pd.read_csv(filename)
    ls = data[col].tolist()
    new_ls = []
    for i in range(n):
        new_ls.append(ls[i])
    return new_ls


if __name__ == "__main__":
    print(return_solutions("sudoku.csv", "solutions", 3))  # to dynamically assign solutions to create a data set
