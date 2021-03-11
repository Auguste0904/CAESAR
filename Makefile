##
## EPITECH PROJECT, 2020
## Crypto-Security
## File description:
## Makefile
##

all:
		cp src/hex_to_base64.py challenge01 && chmod +x challenge01
		cp src/fixed_XOR.py challenge02 && chmod +x challenge02
		cp src/single_byte_XOR.py challenge03 && chmod +x challenge03
		cp src/detect_single_byte_XOR.py challenge04 && chmod +x challenge04
		cp src/repeating_key_XOR.py challenge05 && chmod +x challenge05
		cp src/break_repeating_key_XOR.py challenge06 && chmod +x challenge06
		cp src/AES_in_ECB.py challenge07 && chmod +x challenge07
		cp src/detect_AES_in_ECB.py challenge08 && chmod +x challenge08

clean:
		rm -f challenge01
		rm -f challenge02
		rm -f challenge03
		rm -f challenge04
		rm -f challenge05
		rm -f challenge06
		rm -f challenge07
		rm -f challenge08

fclean:	clean
		rm -f *~

re:	fclean all

.PHONY: all clean fclean re