"""
Primality Testing
This challenge will require a script that will accept an integer and output if it is a Prime Number or not.
Bonus points for outputting composite numbers factors.
"""

def get_int():
    """Asking user for an integer"""
    while True:
        try:
            integer = int(input('Enter an integer: '))
            break
        except ValueError:
            print('Not a valid integer.')
    return integer


def get_factors(integer):
    """Finding factors of an integer"""
    factors_lower = [1]
    factors_higher = [integer]
    i = 2
    while i < min(factors_higher):
        if integer % i == 0:
            factors_lower.append(i)
            factors_higher.insert(0, int(integer/i))
        i += 1
    return factors_lower + factors_higher


if __name__ == '__main__':
    integer = get_int()
    factors = get_factors(integer)
    print('The factors of {} are {}'.format(integer, factors))
    if len(factors) == 2:
        print('The number {} is prime.'.format(integer))
    else:
        print('The number {} is NOT prime.'.format(integer))
