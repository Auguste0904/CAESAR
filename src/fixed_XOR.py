#!/usr/bin/env python3

##
# EPITECH PROJECT, 202 0
# B-SEC-500-PAR-5-1-caesar-lucas.moritel
# File description:
# fixed_XOR.py
##

import os
import string
import sys


def error_gestion_arg(argv):
    if len(argv) != 2:
        print("Error: Invalid number of arguments")
        exit(84)
    if os.path.isfile(argv[1]) == False:
        print("Error: The argument is not a file")
        exit(84)


def main():
    error_gestion_arg(sys.argv)
    file = open(sys.argv[1], "r")
    lines = file.readlines()
    if len(lines) != 2:
        print("Error: Number of lines invalid")
        exit(84)
    # Je retire le '\n' pour qu'il y est 16 charactère et non pas 17
    lines[0] = lines[0].strip('\n')
    # Je retire le '\n' pour qu'il y est 16 charactère et non pas 17
    lines[1] = lines[1].strip('\n')
    if len(lines[0]) % 2 != 0 or len(lines[0]) % 2 != 0:
        print("Error: A line is not event but odd")
        exit(84)
    if len(lines[0]) == 0 or len(lines[1]) == 0:
        print("Error: A line is empty")
        exit(84)
    if len(lines[0]) != len(lines[1]):
        print("Error: Length of lines are different")
        exit(84)
    if all(c in string.hexdigits for c in lines[0]) == 0:
        print("Error: There are no digits in the first line")
        exit(84)
    if all(c in string.hexdigits for c in lines[1]) == 0:
        print("Error: There are no digits in the second line")
        exit(84)
    str = ""
    result = str.join(["%x" % (int(x, 16) ^ int(y, 16))
                       for (x, y) in zip(lines[0], lines[1])])
    print(result.upper())


if __name__ == "__main__":
    main()
