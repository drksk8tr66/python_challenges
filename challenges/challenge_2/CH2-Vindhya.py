
import sys


def force(f: int=0, m: int=0, a: int=0):
    if sum([f, m]) == 0 or sum([f, a]) == 0 or sum([m, a]) == 0:
        print(" Enter at least two variables:")
        sys.exit()
    if f == 0:
        return m * a
    elif m == 0:
        return f / a
    elif a == 0:
        return f / m
    elif f == m * a:
        return "Your calculation is balanced"
    else:
        return "Your equation is not balanced"


if __name__ == '__main__':
    f = int(input('Enter force'))
    m = int(input('Enter mass'))
    a = int(input('enter acceleration'))
    print(force(f, m, a))

# F= M * A


