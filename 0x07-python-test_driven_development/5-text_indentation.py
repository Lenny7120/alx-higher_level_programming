#!/usr/bin/python3
"""
This module contains a function that indent text

"""


def text_indentation(text):
    '''This functions prints a text with 2 lines
    Args:
        text(str): the string to be printed
    Raises:
         TypeError; if the text is not a sting
    '''

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    count = 0
    while count < len(text) and text[count] == " ":
        count = count + 1

    while count < len(text):
        print(text[count], end="")
        if text[count] == "\n" or text[count] in ".?:":
            if text[count] in ".?:":
                print("\n")
            count = count + 1
            while count < len(text) and text[count] == " ":
                count = count + 1
            continue
        count = count + 1
