#!/usr/bin/python3

import sys

def main():
    argv = sys.argv[1:]  # Exclude the script name

    num_arguments = len(argv)
    if num_arguments == 0:
        print("Number of argument(s): .")
    elif num_arguments == 1:
        print("Number of argument(s): argument:")
    else:
        print("Number of argument(s): arguments:")

    print()

    for i, arg in enumerate(argv, start=1):
        print(f"{i}: {arg}")

if __name__ == "__main__":
    main()

