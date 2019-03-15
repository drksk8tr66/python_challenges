
def calc_type(n=None):
    while n not in ['F', 'f', 'M', 'm', 'A', 'a']:
        print("What would you like to calculate? Enter F for Force, M for Mass or A for Acceleration.")
        n = input()
        if n not in ['F', 'f', 'M', 'm', 'A', 'a']:
            print("Input not valid.")
    return n


def get_param(n):
    if n in ('F', 'f'):
        while True:
            var1 = input('Please enter your value for mass in kg.')
            var2 = input('Please enter your value for acceleration in m/s^2.')
            if var1.isnumeric() and var2.isnumeric():
                break
            if not var1.isnumeric() or not var2.isnumeric():
                print('Input not valid')

    if n in ('M', 'm'):
        while True:
            var1 = input('Please enter your value for force in Newtons.')
            var2 = input('Please enter your value for acceleration in m/s^2.')
            if var1.isnumeric() and var2.isnumeric():
                break
            if not var1.isnumeric() or not var2.isnumeric():
                print('Input not valid')

    if n in ('A', 'a'):
        while True:
            var1 = input('Please enter your value for force in Newtons.')
            var2 = input('Please enter your value for mass in kg.')
            if var1.isnumeric() and var2.isnumeric():
                break
            if not var1.isnumeric() or not var2.isnumeric():
                print('Input not valid')

    return var1, var2


def calc_param(n, var1, var2):
    if n in ('F', 'f'):
        f = float(var1) * float(var2)
        print('The calculated force is %s N.' % f)
    if n in ('M', 'm'):
        m = float(var1)/float(var2)
        print('The calculated mass is %s kg.' % m)
    if n in ('A', 'a'):
        a = float(var2)/float(var1)
        print('The calculated acceleration is %s m/s^2.' % a)
    return

calctype = calc_type()
v1, v2 = get_param(calctype)
calc_param(calctype, v1, v2)
