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

# swap key/values in dict
morse_decode = {value : key for key, value in morse_code.items()}

r = input("Would you like to send (S) or receive (R) a message?")

# send message
if r.upper() == "S":
    
    schar = ""
    send_string = input("Please enter your message \n")
    
    for x in itertools.chain(send_string):
        # iterate over each character and map to code
        schar = schar + morse_code[x]
    
    print("Your message is:\n%s" % schar)


# receive message
elif r.upper() == "R":
    
    rchar = ""
    
    received = input("Please paste your code:").upper()
    split_words = received.split(" / ")  # split by word
    
    for x in split_words:

        # split by coded character
        split_chars = x.split(" ") 
        word_str = ""
        
        for y in split_chars:
            # map code to character and add to the end of word string
            word_str = word_str + morse_decode[y] 

        rchar = rchar + word_str + " " # add each word to the message string
    
    print("Your message is:\n%s" % rchar)