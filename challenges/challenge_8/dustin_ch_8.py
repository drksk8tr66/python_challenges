

def arrange_message(words: int=0, msg: str=None):
    if not msg:
        msg = input("please type you message here")
    if msg.isnumeric():
        digits = []
        for i in range(len(str(msg))):
            digits.append(str(msg)[i])
            digits.sort()
        print(digits)
        return digits
    else:
        if words == 0:
            new_msg = sorted([msg.split(' ')])
            print(new_msg)
            return new_msg
        else:
            chars = []
            for i in range(len(msg)):
                chars.append(msg[i])
                chars.sort()
            print(chars)
            return chars


if __name__ == '__main__':
    arrange_message(1, "123")



