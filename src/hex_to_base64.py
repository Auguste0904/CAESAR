#!/usr/bin/env python3

##
## EPITECH PROJECT, 2020
## B-SEC-500-PAR-5-1-caesar-lucas.moritel
## File description:
## hex_to_base64.py
##

import codecs
import os
import string
import sys

def hex_to_base64(file):
    isEncoded = codecs.encode(codecs.decode(file, 'hex'), 'base64')
    isEncoded = codecs.decode(isEncoded)
    isEncoded = isEncoded.replace('\n', '')
    print(isEncoded)

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
    fileContent = file.read()
    if fileContent == "":
        print("Error: File is empty")
        exit(84)
    fileContent = fileContent.replace('\n', '')
    if all(c in string.hexdigits for c in fileContent) == False:
        print("Error: No hexadecimal base")
        exit(84)
    contentSize = len(fileContent) % 2
    if contentSize != 0:
        print("Error: Length of the file content is not even but odd")
        exit(84)
    hex_to_base64(fileContent)

if __name__ == "__main__":
    main()
