#!/usr/bin/env python3

##
# EPITECH PROJECT, 2020
# B-SEC-500-PAR-5-1-caesar-lucas.moritel
# File description:
# AES_in_ECB.py
##

import sys
import os
import base64
import string
from Crypto.Cipher import AES


def error_gestion_arg(argv):
    if len(argv) != 2:
        print("Error: Invalid number of arguments")
        exit(84)
    if os.path.isfile(argv[1]) == False:
        print("Error: The argument is not a file")
        exit(84)


def decrypt_aes_in_ecb(key, text):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(text)[:-ord(cipher.decrypt(text)[len(cipher.decrypt(text)) - 1:])]


def main():
    error_gestion_arg(sys.argv)
    file = open(sys.argv[1])
    hexa_key = file.readline().strip('\n')
    if (len(hexa_key) == 0 or hexa_key == ''):
        print("Error: The key is missing")
        exit(84)
    if len(hexa_key) % 16 != 0:
        print("Error: Invalid key size")
        exit(84)
    if all(chara in string.hexdigits for chara in hexa_key) == False:
        print("Error: The key has no hexadecimal base")
        exit(84)
    text = file.readline().strip('\n')
    if len(text) == 0 or text == '':
        print("Error: The text is missing")
        exit(84)
    if (type(text) == base64):
        print("Error: The text is invalid")
        exit(84)
    key = bytes.fromhex(''.join(hexa_key).encode().decode())
    text = base64.b64decode(''.join(text).encode())
    ciphertext = decrypt_aes_in_ecb(key, text)
    result = base64.b64encode(ciphertext)
    print(result.decode('utf-8'))


if __name__ == '__main__':
    main()
