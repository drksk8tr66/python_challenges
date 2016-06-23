'''
Calculator for force, mass, and acceleration
https://www.reddit.com/r/dailyprogrammer/comments/pjbj8/easy_challenge_2/
'''


def which_calculation(c='Unknown'):
    options = ['F', 'f', 'M', 'm', 'A', 'a']
    while c not in options:
        print('Enter F if you would like to calculate force.')
        print('Enter M if you would like to calculate mass.')
        print('Enter A if you would like to calculate acceleration.')
        c = input()
        if c in ('Q', 'q'):
            exit()
        if c not in options:
            print('Valid input not entered.')
    return c


def ask_parameters(c):
    print('Please enter only scalar quantities for the following.')
    f = 'unknown'
    m = 'unknown'
    a = 'unknown'

    if c not in ('F', 'f'):
        while not f.isnumeric():
            f = input('Enter the value for force (in Newtons):')
            if f in ('Q', 'q'):
                exit()
            if not f.isnumeric():
                print('Valid number not entered')

    if c not in ('M', 'm'):
        while not m.isnumeric():
            m = input('Enter the value for mass (in kilograms):')
            if m in ('Q', 'q'):
                exit()
            if not m.isnumeric():
                print('Valid number not entered')

    if c not in ('A', 'a'):
        while not a.isnumeric():
            a = input('Enter the value for acceleration (in m/s^2):')
            if a in ('Q', 'q'):
                exit()
            if not a.isnumeric():
                print('Valid number not entered')

    return f, m, a


def calculate_and_display_results(c, f, m, a):
    if c in ('F', 'f'):
        f = float(m) * float(a)
        print('The calculated force is %s N.' % f)
    elif c in ('M', 'm'):
        m = abs(float(f) / float(a))
        print('The calculated mass is %s kg.' % m)
    elif c in ('A', 'a'):
        a = float(f) / float(m)
        print('The calculated acceleration is %s m/s^2.' % a)
    return


print('Welcome to the Force/Mass/Acceleration Calculator.')
print('Enter "Q" at any point to exit the program.\n')
calculate = which_calculation()
force, mass, acceleration = ask_parameters(calculate)
calculate_and_display_results(calculate, force, mass, acceleration)
