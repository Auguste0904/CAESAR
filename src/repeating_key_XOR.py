#!/usr/bin/env python3

##
## EPITECH PROJECT, 2020
## B-SEC-500-PAR-5-1-caesar-lucas.moritel
## File description:
## repeating_key_XOR.py
##

import os
import sys
import codecs

def error_gestion_arg(argv):
    if len(argv) != 2:
        print("Error: Invalid number of arguments")
        exit(84)
    if os.path.isfile(argv[1]) == False:
        print("Error: The argument is not a file")
        exit(84)

def repeating_key_xor(key, text):
    output = b''
    i = 0
    for chara in text:
        output += bytes([chara ^ key[i]])
        if (i + 1) == len(key):
            i = 0
        else:
            i += 1
    return output

def main():
    error_gestion_arg(sys.argv)
    file = open(sys.argv[1], "r")
    encoded_key = file.readline().strip('\n')
    encoded_text = file.readline().strip('\n')
    if len(encoded_key) == 0:
        print("Error: There is no key in your file")
        exit(84)
    if len(encoded_text) == 0:
        print("Error: There is no text to decrypt in your file")
        exit(84)
    size_key = len(encoded_key) % 2
    if size_key != 0:
        print("Error: Length of the encoded key content is not even but odd")
        exit(84)
    if encoded_text == '' or encoded_key == '':
        print("Error: The encoded key or the encoded tesxt is missing")
        exit(84)
    decoded_text = ''.join(encoded_text).encode()
    decoded_key = ''.join(encoded_key).encode()
    decoded_text = codecs.decode(decoded_text, 'hex')
    decoded_key = codecs.decode(decoded_key, 'hex')
    ciphertext = repeating_key_xor(decoded_key, decoded_text)
    print(ciphertext.hex().upper())

if __name__ == "__main__":
    main()
