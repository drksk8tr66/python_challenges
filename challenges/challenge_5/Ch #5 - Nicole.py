'''
Calculating Pi
https://www.reddit.com/r/dailyprogrammer/comments/pp53w/2142012_challenge_6_easy/

Chudnovsky's Algorithm (>14 digits per iteration)
https://en.wikipedia.org/wiki/Chudnovsky_algorithm
'''

import math
import decimal


def chudnovsky(i, n):
    # Using the decimal module and setting precision (adding ten to prevent rounding errors)
    # This prevents us from losing precision/accuracy in calculations
    decimal.getcontext().prec = n + 10

    # Calculating the summation portion of the Chudnovsky algorithm
    s = 0
    for k in range(0, i):
        s += decimal.Decimal(((-1) ** k * math.factorial(6 * k) * (545140134 * k + 13591409)) / decimal.Decimal(
            math.factorial(3 * k) * math.factorial(k) ** 3 *
            decimal.Decimal((640320 ** 3) ** (decimal.Decimal(k + decimal.Decimal(0.5))))))

    # Calculating the rest of the Chudnovsky algorithm and returning the results
    pi = decimal.Decimal(1 / decimal.Decimal(12 * s))
    return round(pi, n)


def main():
    print('Enter Q at any time to exit the program.\n')

    # Finding out how many digits the user wants
    num_digits = 'unknown'
    while not num_digits.isnumeric():
        num_digits = input('How many decimal digits of pi would you like to generate? ')
        if num_digits in ('Q', 'q'):
            exit()
        if not num_digits.isnumeric():
            print('Valid number not entered.')
    num_digits = int(num_digits)

    # How many times we need to call the Chudnovsky algorithm
    # Each iteration calculates >14 digits
    iterations = math.ceil(num_digits / 14)

    # Calling the function to calculate pi and displaying the results
    print('Here is pi rounded to %s decimal digits:' % num_digits)
    print(chudnovsky(iterations, num_digits))


if __name__ == "__main__":
    main()
