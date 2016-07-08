import random


def generate_pw(num, min_char: int=8, max_char: int=28):
    if min_char < 8:

    pws = []
    s = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ']', '[', ')']
    while len(pws) < num:
        l = random.randrange(min_char, max_char, 1)
        x = ''.join(random.sample("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*(][)", l))
        counts = {'upper': 0, 'lower': 0, 'number': 0, 'special': 0}
        for c in x:
            if c.isupper():
                counts['upper'] += 1
            elif c.islower():
                counts['lower'] += 1
            elif c.isdigit():
                counts['number'] += 1
            elif c in s:
                counts['special'] += 1
        if counts['upper'] >= 2 and counts['lower'] >= 2 and counts['number'] >= 2 and counts['special'] >= 2:
            pws.append(x)
        else:
            continue
    return pws

print(generate_pw(3))
