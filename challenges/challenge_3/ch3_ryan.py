#!/usr/bin/env python3
"""
# https://www.reddit.com/r/dailyprogrammer/comments/pkw2m/2112012_challenge_3_easy/

For this challenge we are writing a Caesar Cipher!
A Caesar Cipher assigns letters in a text string to different letters in the
Alphabet.
Ex. A=B, B=C, C=D, etc…
Bonus Points for writing a decrypt function to our program!


This is very cool, and I want to kick it up a notch!
Let’s all agree on the same cipher to use, so that we can send messages to
each other and then be able to translate them.
Here is the Cipher we shall use for this challenge.
Input Text	Cipher Text
A	Y
B	P
C	L
D	T
E	A
F	V
G	K
H	R
I	E
J	Z
K	G
L	M
M	S
N	H
O	U
P	B
Q	X
R	N
S	C
T	D
U	I
V	J
W	F
X	Q
Y	O
Z	W
"""

from functools import partial
from string import ascii_letters
from pathlib import Path

CIPHER = bytearray("YPLTAVKREZGMSHUBXNCDIJFQOW", 'ascii')
CIPHER[0:0] = CIPHER.lower()
ASCII_BARRAY = bytearray(ascii_letters, 'ascii')


def crypt(from_group, to_group, message):
    """Encrypt message with cypher, or decrypt"""
    if isinstance(message, str):
        message = bytes(message, 'ascii')
    trans = bytes.maketrans(from_group, to_group)
    return bytes.decode(message.translate(trans), 'ascii')


ENCRYPT = partial(crypt, ASCII_BARRAY, CIPHER)
DECRYPT = partial(crypt, CIPHER, ASCII_BARRAY)


if __name__ == '__main__':
    print(DECRYPT(
        Path('Secret Message_encrypted.txt').read_bytes()))
