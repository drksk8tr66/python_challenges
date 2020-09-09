
# https://www.reddit.com/r/dailyprogrammer/comments/pjbj8/easy_challenge_2/
import sys


def solve_force(f: int=0, m: int=0, a: int=0):
    if sum([f, m]) == 0 or sum([m, a]) == 0 or sum([f, a]) == 0:
        print("Please include at least 2 variables to solve for the 3rd")
        sys.exit()
    if f == 0:
        return m * a
    elif m == 0:
        return f / a
    elif a == 0:
        return f / m
    elif f == m * a:
        return "your equation is balanced : " + str(f) + " = " + str(m) + " * " + str(a)
    else:
        return "your equation is unbalanced"


if __name__ == '__main__':
    print(solve_force(m=2, a=1, f=0))
    # pass

