import itertools

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
              ' ':' / '}

morse_decode = {value : key for key, value in morse_code.items()}

r = input("Would you like to send (S) or receive (R) a message?")

if r.upper() == "S":
    
    schar = ""
    send_string = input("Please enter your message \n")
    
    for x in itertools.chain(send_string):
        schar = schar + morse_code[x]
    
    print("Your message is:\n%s" % schar)

elif r.upper() == "R":
    
    rchar = ""
    received = input("Please paste your code:").upper()
    split_words = received.split(" / ")
    
    for x in split_words:
        
        split_chars = x.split(" ")
        word_str = ""
        
        for y in split_chars:
            
            word_str = word_str + morse_decode[y]
        
        rchar = rchar + word_str + " "
    
    print("Your message is:\n%s" % rchar)