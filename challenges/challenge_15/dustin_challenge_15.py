from decimal import *
import math


def divide(num=8675309):
    """ Trial Division """
    i = 2
    sqrt = Decimal(math.sqrt(num))
    factors = []
    while i <= sqrt:
        x = Decimal(num) / Decimal(i)
        frac, whole = math.modf(x)
        if frac == 0:
            factors.append(i)
            factors.append(int(Decimal(num) / Decimal(i)))
        i += 1
    if not factors:
        factors = "{0} is a Prime Number".format(num)
    return "Factors of {0}".format(num), factors


if __name__ == '__main__':
    print(divide())
