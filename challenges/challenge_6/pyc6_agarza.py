""" morse dicts """
morse_code = {'A':'.-',
              'B':'-...',
              'C':'-.-.',
              'D':'-..',
              'E':'.',
              'F':'..-.',
              'G':'--.',
              'H':'....',
              'I':'..',
              'J':'.---',
              'K':'-.-',
              'L':'.-..',
              'M':'--',
              'N':'-.',
              'O':'---',
              'P':'.--.',
              'Q':'--.-',
              'R':'.-.',
              'S':'...',
              'T':'-',
              'U':'..-',
              'V':'...-',
              'W':'.--',
              'X':'-..-',
              'Y':'-.--',
              'Z':'--..',
              '0':'-----',
              '1':'.----',
              '2':'..---',
              '3':'...--',
              '4':'....-',
              '5':'.....',
              '6':'-....',
              '7':'--...',
              '8':'---..',
              '9':'----.',
              ' ':'/'}

morse_decode = {value : key for key, value in morse_code.items()}


    
def morse_receive():  
    """ receive - dash/dot to character """
    received = input('Please paste your code: ').upper()
    split_chars = received.split(' ')
    message = ''.join(map(morse_decode.get, split_chars))   
    print(message)

def morse_send():
    """ send - character to dash/dot """
    send = input('Please enter your message: ').upper()
    message = ' '.join(map(morse_code.get, send))    
    print(message)



def main():

    while True:
        send_rec = input('Would you like to send (S) or receive (R) a message? ')
        if send_rec.upper() in ('S','R'):
            break
    
    if send_rec == 'S':
        morse_send()
        
    elif send_rec == 'R':
        morse_receive()
        
    else: print('Error')

    
if __name__ == '__main__':
    main()