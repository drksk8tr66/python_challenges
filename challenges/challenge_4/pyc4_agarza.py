import string
import random


def num_pw(): # request generated passwords
    while True:
        
        pw_distinct = input('How many passowrds would you like to generate? ')
        if pw_distinct.isdigit():
            return int(pw_distinct)
            break


def len_pw(): # set password length
    while True:
        pw_length = input('Password length: ')
        if pw_length.isdigit():
            return int(pw_length)
            break
    

def gen_pw(l): # generate passwords    
    
    print_all = list(string.printable)[:94]
    pw = ''.join(random.choices(print_all, k=l))
    
    return pw

   
def score_pw(p): # score password
    
    pw = p
    
    print_num = list(string.printable[:10])
    print_lc = list(string.printable[10:36])
    print_uc = list(string.printable[36:62])
    print_sc = list(string.printable[62:])

    pw_score = 0    
    if any(j in pw for j in print_lc): pw_score += 1
    if any(j in pw for j in print_uc): pw_score +=1
    if any(j in pw for j in print_num): pw_score += 1
    if any(j in pw for j in print_sc): pw_score += 1
    
    if pw_score <= 2: pw_strength = 'Password Strength is LOW'
    elif pw_score == 3: pw_strength = 'Password Strength is MODERATE'
    elif pw_score == 4: pw_strength = 'Password Strength is STRONG'
    else: 'ERROR'
    
    return pw_strength


def main():
    
    n = num_pw()
    l = len_pw()
    
    for x in range(n):
        pw = gen_pw(l)
        score = score_pw(pw)
        print('{}  -  {}'.format(pw, score))

if __name__ == '__main__':
    main()