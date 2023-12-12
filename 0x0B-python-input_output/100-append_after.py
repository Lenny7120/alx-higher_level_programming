#!/usr/bin/python3
"""
python module
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after each line containing a
    specific string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line.
        new_string (str): The line of text to insert after the line
        with the search string.

    Returns:
        None
    """
    lines = []
    with open(filename, "r") as file:
        for line in file:
            lines.append(line)
            if search_string in line:
                lines.append(new_string + "\n")

    with open(filename, "w") as file:
        file.writelines(lines)


def append_after(filename="", search_string="", new_string=""):
   """
   Inserts a line of text after each line containing a
   specific string in a file.

   Args:
       filename (str): The name of the file.
       search_string (str): The string to search for in each line.
       new_string (str): The line of text to insert after the line
       with the search string.

   Returns:
       None
   """
   with open(filename, "r", encoding="utf-8") as file:
       line_list = file.readlines()

   with open(filename, "w", encoding="utf-8") as file:
       for line in line_list:
           file.write(line)

           if search_string in line:
               file.write(new_string)
