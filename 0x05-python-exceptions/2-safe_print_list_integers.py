#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    total_count = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                total_count += 1
            else:
                continue
        except IndexError:
            break
    print()
    return total_count
