#!/usr/bin/python3
if __name__ == "__main__":
    import sys

total = 0
for argument in sys.argv[1:]:
    total += int(argument)

print(total)
