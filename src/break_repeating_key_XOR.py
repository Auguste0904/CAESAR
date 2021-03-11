#!/usr/bin/env python3

##
# EPITECH PROJECT, 2020
# B-SEC-500-PAR-5-1-caesar-lucas.moritel
# File description:
# break_repeating_key_XOR.py
##

import sys
import codecs
import os
import string

def error_gestion_arg(argv):
    if len(argv) != 2:
        print("Error: Invalid number of arguments")
        exit(84)
    if os.path.isfile(argv[1]) == False:
        print("Error: The argument is not a file")
        exit(84)

def single_char_xor(byte_array_1, byte_array_2):
    result = bytearray(len(byte_array_1))
    for i in range(len(byte_array_1)):
        result[i] = byte_array_1[i] ^ byte_array_2[i]
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

def set_beside_byte(byte_array_1, byte_array_2):
    beside_byte = 0
    for single_byte in single_char_xor(byte_array_1, byte_array_2):
        beside_byte += bin(single_byte).count("1")
    return beside_byte

def get_key_size(byte):
    nb_break = []
    for KEYSIZE in range(5, 41):
        byte_array_1 = byte[: KEYSIZE]
        byte_array_2 = byte[KEYSIZE: KEYSIZE * 2]
        byte_array_3 = byte[KEYSIZE * 2: KEYSIZE * 3]
        byte_array_4 = byte[KEYSIZE * 3: KEYSIZE * 4]
        single_break = float(set_beside_byte(byte_array_1, byte_array_2) + set_beside_byte(byte_array_2, byte_array_3) + set_beside_byte(byte_array_3, byte_array_4)) / (KEYSIZE * 3)
        nb_break.append((KEYSIZE, single_break))
    nb_break = sorted(nb_break, key=lambda x: x[1])
    return nb_break

def break_single_key_xor(byte_array_1):
    key = None
    max_frequency_score = 0
    for i in range(256):
        byte_array_2 = len(byte_array_1) * [i]
        plaintext = bytes(single_char_xor(byte_array_1, byte_array_2))
        current_frequency_score = score(plaintext)
        if max_frequency_score == 0 or current_frequency_score > max_frequency_score:
            max_frequency_score = current_frequency_score
            key = bytes([i])
    return key

def main():
    error_gestion_arg(sys.argv)
    file = open(sys.argv[1], "r")
    fileContent = file.read().replace('\n', '')
    if fileContent == '':
        print("Error: This file is empty")
        exit(84)
    if all(chara in string.hexdigits for chara in fileContent) == False:
        print("Error: No hexadecimal base")
        exit(84)
    hexa_byte = bytearray.fromhex(fileContent)
    nb_break = get_key_size(hexa_byte)
    result = None
    max_frequency_score = 0
    for KEYSIZE, j in nb_break:
        bytes_block = [[] for j in range(KEYSIZE)]
        for i, single_byte in enumerate(hexa_byte):
            bytes_block[i % KEYSIZE].append(single_byte)
        all_keys = b""
        for nb_byte in bytes_block:
            all_keys += break_single_key_xor(nb_byte)
        final_key = bytearray(all_keys * len(hexa_byte))
        if (final_key == None):
            print("Error: The key was filled badly")
        plaintext = bytes(single_char_xor(hexa_byte, final_key))
        if score(plaintext) > max_frequency_score or max_frequency_score == 0:
            result = codecs.decode(codecs.encode(all_keys, 'hex')).upper()[:KEYSIZE]
            max_frequency_score = score(plaintext)
    print(result)

if __name__ == '__main__':
    main()
