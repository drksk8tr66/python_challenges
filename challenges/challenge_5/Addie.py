"""
Using Chudnovsky's formula to calculate pi.

Chudnovsky's formula/algorithm was published by the Chudnovsky brothers who were American mathematicians.

More info: https://en.wikipedia.org/wiki/Chudnovsky_algorithm
"""

from math import factorial
from decimal import Decimal, getcontext


def get_dec():
    a = input('How many decimal places for pi do you want?')
    while not a.isdigit():
        if a.isalpha() or a.isalnum():
            print('Input not valid. Please enter a number.')
            a = input('How many decimal places for pi do you want?')
    return a


n = int(get_dec())
getcontext().prec = n + 1


def calc(n):
    pi = Decimal(0)
    num = Decimal(0)
    denom = Decimal(0)
    k = 0

    num = (-1)**k * (factorial(6*k)) * ((545140134 * k) + 13591409)
    denom = factorial(3*k) * (factorial(k)**3) * (640320**Decimal((3*k) + 1.5))
    pi += Decimal(12) * (Decimal(num)/Decimal(denom))
    pi = 1/pi
    return pi


print(calc(n))
print(len(str(calc(n))))
