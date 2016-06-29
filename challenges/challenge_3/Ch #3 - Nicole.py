'''
Caesar Cypher
https://www.reddit.com/r/dailyprogrammer/comments/pkw2m/2112012_challenge_3_easy/
'''

import sys  # This is used so we can accept multiline input


def encrypt(a=[], c=[], m=[]):
    n = ''
    for i in range(0, len(m)):
        try:
            a_index = a.index(m[i])
            n = n + c[a_index]
        except ValueError:
            n = n + m[i]
    return n


def decrypt(a=[], c=[], m=[]):
    n = ''
    for i in range(0, len(m)):
        try:
            c_index = c.index(m[i])
            n = n + a[c_index]
        except ValueError:
            n = n + m[i]
    return n


def main():
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    cipher = ['Y', 'P', 'L', 'T', 'A', 'V', 'K', 'R', 'E', 'Z', 'G', 'M', 'S', 'H', 'U', 'B', 'X', 'N', 'C', 'D', 'I',
              'J', 'F', 'Q', 'O', 'W']

    print('Enter the message you would like to encrypt/decrypt.  When finished, press Enter, then CTRL+D')
    message = list(sys.stdin.read().upper())
    print('\n')
    print('Encrypted message: ', encrypt(alphabet, cipher, message))
    print('Decrypted message: ', decrypt(alphabet, cipher, message))


if __name__ == "__main__":
    main()
