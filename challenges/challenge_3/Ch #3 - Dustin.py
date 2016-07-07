
# https://www.reddit.com/r/dailyprogrammer/comments/pkw2m/2112012_challenge_3_easy/

cipher = {'a': 'y', 'b': 'p', 'c': 'l', 'd': 't', 'e': 'a', 'f': 'v', 'g': 'k', 'h': 'r', 'i': 'e', 'j': 'z', 'k': 'g',
          'l': 'm', 'm': 's', 'n': 'h', 'o': 'u', 'p': 'b', 'q': 'x', 'r': 'n', 's': 'c', 't': 'd', 'u': 'i', 'v': 'j',
          'w': 'f', 'x': 'q', 'y': 'o', 'z': 'w'}

r_cipher = {v: k for k, v in cipher.items()}


def encrypt_file(fname):
    f = open(fname, 'r')
    e = open(fname.replace('.txt', '') + '_encrypted' + '.txt', 'w', newline='')
    for l in f.readlines():
        e.write(encrypt(l))


def decrypt_file(fname):
    f = open(fname, 'r')
    e = open(fname.replace('.txt', '') + '_decrypted' + '.txt', 'w', newline='')
    for l in f.readlines():
        e.write(decrypt(l))


def encrypt(msg):
    e_text = ''.join(cipher.get(char, char) for char in msg.lower())
    return e_text


def decrypt(msg):
    d_text = ''.join(r_cipher.get(char, char) for char in msg.lower())
    return d_text


if __name__ == '__main__':
    # pass
    # encrypt_file('Secret Message')
    decrypt_file('Secret Message_encrypted.txt')
