import argparse
import sys

class Crypto:
    '''
    A wrapper for the maketrans function used in our context 
    '''
    def __init__(self, alphabet, cipher):
        self.alpha = alphabet
        self.cipher = cipher
        return		
	
    def encode(self, msg=''):
        return msg.translate(str.maketrans(self.alpha, self.cipher))
        
    def decode(self, msg=''):
	    return msg.translate(str.maketrans(self.cipher, self.alpha))

def read_msg(filepath=''):
    lines = []
    try:
        secret_msg = open(filepath)
        for line in secret_msg:
            lines.append(line.rstrip())
        secret_msg.close()
        return lines
    except:
        raise Exception('Oops...something went wrong reading the . This computer will self destruct in 10 seconds..')
	
if __name__ == '__main__':
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    cipher = 'YPLTAVKREZGMSHUBXNCDIJFQOWypltavkrezgmshubxncdijfqow'
    c = Crypto(alpha, cipher)
    print(sys.argv[1])
    try:
        for l in read_msg(sys.argv[1]):
            print(c.decode(l))
    except Exception as e:
        print(e)
