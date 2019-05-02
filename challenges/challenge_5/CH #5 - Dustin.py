"""
I have found a few methods for estimating and calculating pi of varying accuracies
investigating how to calculate this currently # (1/2)! = sqrt(pi)/2
"""

from decimal import *  # Decimal, getcontext, setcontext, Context
import math


def gamma_method():
    # 14 decimals of accuracy
    context = Context(prec=13, flags=[Rounded, Inexact])
    setcontext(context)
    g_pi = Decimal(math.gamma(0.5)**2)
    print(g_pi)
    print(str(g_pi)[:16])


def stolen_method():
    """
    Literally stole this from the internet, no clue how it works
    https://www.reddit.com/r/dailyprogrammer/comments/pp53w/2142012_challenge_6_easy/c3r4xlm?utm_source=share&utm_medium=web2x
    """
    places = input("How many decimal places do you want? :")
    while not places.isdigit():
        if places.upper() == 'Q':
            exit()
        else:
            places = input("Please Enter a number for how many decimal places do you want?, or Enter Q to quit :")

    places = int(places)
    getcontext().prec = places + 1
    m = 10

    a = [0]*m
    b = [0]*m
    t = [0]*m
    p = [0]*m

    one = Decimal(1)
    two = Decimal(2)
    four = Decimal(4)
    half = one/two

    a[0] = one
    # b0 = sqrt(2)/2
    b[0] = one/two**(one/two)
    t[0] = one/four
    p[0] = one

    lastpi = 0

    for n in range(m-1):
        # 1/2(1+1/sqrt(2))
        a[n+1] = (a[n]+b[n])/two
        #
        b[n+1] = (a[n]*b[n])**half
        t[n+1] = t[n] - p[n]*(a[n]-a[n+1])**2
        p[n+1] = two*p[n]
        pi = (a[n+1] + b[n+1])**2/four/t[n+1]
        if lastpi == pi:
            breakpoint()
        lastpi = pi

    print('Pi calculated in', n, 'loops, as', pi)


if __name__ == '__main__':
    gamma_method()
    # stolen_method()
