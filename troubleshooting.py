row_test = [8, 6, 4, 3, 7, 1, 2, 5, 9]

def val_range(t_item):
    c = 0
    for item in t_item:
        if item>=1 and item<=9:
            c = c +1
    if c != 9:
        return False
    else:
        return True


val_range(row_test)
