import random


def generate_pw(num):
    pws = []
    s = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ']', '[', ')']
    while len(pws) < num:
        l = random.randrange(8, 28, 1)
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
