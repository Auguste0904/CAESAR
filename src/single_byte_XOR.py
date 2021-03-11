#!/usr/bin/env python3

##
## EPITECH PROJECT, 2020
## B-SEC-500-PAR-5-1-caesar-lucas.moritel
## File description:
## single_byte_XOR.py
##

import os
import string
import sys
import codecs

def error_gestion_arg(argv):
    if len(argv) != 2:
        print("Error: Invalid number of arguments")
        exit(84)
    if os.path.isfile(argv[1]) == False:
        print("Error: The argument is not a file")
        exit(84)

def single_char_xor(byt_earray_1, byt_earray_2):
    result = bytearray(len(byt_earray_1))
    for i in range(len(byt_earray_1)):
        result[i] = byt_earray_1[i] ^ byt_earray_2[i]
    return result

def score(input_bytes):
    character_frequencies = {
        ' ': 0.13,
        'e': 0.12702,
        't': 0.091,
        'a': 0.082,
        'o': 0.075,
        'i': 0.07,
        'n': 0.067,
        's': 0.063,
        'h': 0.061,
        'r': 0.06,
        'd': 0.043,
        'l': 0.04,
        'c': 0.028,
        'u': 0.028,
        'm': 0.024,
        'w': 0.024,
        'f': 0.022,
        'g': 0.02,
        'y': 0.02,
        'p': 0.019,
        'b': 0.015,
        'v': 0.0098,
        'k': 0.0077,
        'j': 0.0015,
        'x': 0.0015,
        'q': 0.00095,
        'z': 0.00074
    }
    return sum([character_frequencies.get(chr(byte), 0) for byte in input_bytes.lower()])

def main():
    error_gestion_arg(sys.argv)
    file = open(sys.argv[1], "r")
    fileContent = file.read().strip()
    if fileContent == "":
        print("Error: File is empty")
        exit(84)
    fileContent = fileContent.replace('\n', '')
    if all(chara in string.hexdigits for chara in fileContent) == False:
        print("Error: No hexadecimal base")
        exit(84)
    contentSize = len(fileContent) % 2
    if contentSize != 0:
        print("Error: Length of the file content is not even but odd")
        exit(84)
    byt_earray_1 = bytearray.fromhex(fileContent)
    max_frequency_score = 0
    key = 0
    for i in range(256):
        byt_earray_2 = [i] * len(byt_earray_1)
        encrypted_content = bytes(single_char_xor(byt_earray_1, byt_earray_2))
        current_frequency_score = score(encrypted_content)
        if max_frequency_score == 0 or current_frequency_score > max_frequency_score:
            max_frequency_score = current_frequency_score
            key = bytes([i])
    final_key = codecs.decode(codecs.encode(key, 'hex'), 'utf-8')
    print(final_key.upper())

if __name__ == "__main__":
    main()
