#  Calculate pi using Gauss-Legendre algoritm
#  Converges to 45 million correct digits of pi after only 25 iterations.
#  https://en.wikipedia.org/wiki/Gauss–Legendre_algorithm

import decimal 
import numpy as np

 # set precision

def set_prec():
    while True:
        p = input('Set level of precision: ')
        if p.isdigit():
            return int(p)
            break
        else:
            print('Please enter a whole number.')

def main():
    
    prec = set_prec()
    dec = decimal.Decimal
    decimal.getcontext().prec = prec

    # initial values
    a0 = 1
    b0 = 1 / np.sqrt(dec(2))
    t0 = 1 / dec(4)
    p0 = 1

    # iterate while values are more than desired the desired level of precision
    while np.abs(a0 - b0) > 10**(-prec):

        a1 = (a0 + b0)/2
        b1 = np.sqrt(a0*b0)
        t1 = t0 - p0*(a0 - a1)**2
        p1 = 2 * p0

        pi = (a1 + b1)**2 / (4*t1)

        # reset values for next iteration
        a0 = a1
        b0 = b1
        t0 = t1
        p0 = p1

    print(pi)

if __name__ == '__main__':
    main()