#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        last_num = number % -(10)
        print(-(last_num), end='')
    else:
        last_num = number % 10
        print(last_num, end='')
    return abs(last_num)
