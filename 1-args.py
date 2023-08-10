#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num_args = len(argv) - 1  # Subtracting 1 to exclude the script name itself

    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_args))

    for i in range(1, num_args + 1):
        print("{}: {}".format(i, argv[i]))
