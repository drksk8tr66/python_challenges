#!/usr/bin/env python3
"""
# https://www.reddit.com/r/dailyprogrammer/comments/pjbj8/easy_challenge_2/

Hello, coders! An important part of programming is being able to apply your
programs.  So your challenge for today is to create a calculator application
that has use in your life.
We will be making a Force Calculator using F = M * A.
EXTRA CREDIT: make the calculator have multiple functions!  Not only should
it be able to calculate F = M * A, but also A = F/M, and M = F/A!  """

from decimal import Decimal as d
from decimal import InvalidOperation


def calc_what():
    """Figure out what thing to calculate"""
    choices = {'f': 'Force', 'm': 'Mass', 'a': 'Acceleration'}
    what = input(
        'Which would you like to calculate? (F)orce, (M)ass, or (A)cceleration'
        '\nEnter the letter in parenthesis: ')
    try:
        solve_for = choices.pop(what.lower())
    except KeyError:
        print("The only valid choices are 'F', 'M', or 'A'")
        calc_what()
    output = get_entries(choices)
    print("{solve_for} is {output:,.3f}".format(**locals()))
    exit()  # otherwise earlier errors will unroll


def get_entries(things):
    """Get the values"""
    F = None
    M = None
    A = None
    try:
        for each in things:
            thing = d(input("Enter {}: ".format(things[each])))
            if 'f' in each:
                F = thing
            if 'm' in each:
                M = thing
            if 'a' in each:
                A = thing
    except InvalidOperation:
        print("All entries must be a number.")
        calc_what()
    return calculate(F, M, A)


def calculate(F=None, M=None, A=None):
    """Calculate force or the missing component"""
    if not F:
        return M * A
    return F / sum([x for x in [M, A] if x])


if __name__ == '__main__':
    calc_what()
