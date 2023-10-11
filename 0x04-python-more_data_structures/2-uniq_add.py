#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_integers = set()
    total = 0
    for number in my_list:
        if number not in uniq_integers:
            uniq_integers.add(number)
            total += number
    return total
