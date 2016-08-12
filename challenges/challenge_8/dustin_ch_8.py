

def arrange_message(words: int=0):
    msg = input("please type you message here")
    if msg.isnumeric():
        digits = []
        for i in range(len(str(msg))):
            digits.append(str(msg)[i])
            digits.sort()
        for digit in digits:
            print(digit)
    else:
        if words == 0:
            new_msg = sorted([msg.split(' ')])
            print(new_msg)
        else:
            chars = []
            for i in range(len(msg)):
                chars.append(msg[i])
                chars.sort()
            for x in chars:
                print(x)



if __name__ == '__main__':
    arrange_message(1)
    #is_alphabetical(get_inputs())



