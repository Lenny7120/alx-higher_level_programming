#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0  # Initialize a counter for the number of integers printed

    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")  # Print the integer with formatting
                count += 1
        print()  # Print a new line after all integers
    except IndexError:
        pass  # Handle the case when x is larger than the list length quietly

    return count 
