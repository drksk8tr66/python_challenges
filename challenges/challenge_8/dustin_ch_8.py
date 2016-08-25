import cmath

def arrange_message(msg):
    nums = [int, float]
    chars = []
    digits = []
    sorted_msg = []
    for i in msg:
        if type(i) in nums:
            digits.append(i)
        elif type(i) == complex:
            digits.append(cmath.phase(i))
        else:
            chars.append(i)
    chars.sort()
    digits.sort()
    if digits:
        sorted_msg = digits
        for i in chars:
            sorted_msg.append(i)
    elif chars:
        sorted_msg = chars
    return sorted_msg



if __name__ == '__main__':
    arrange_message([1, 2, 3, 'a', 'b', 'c'])



