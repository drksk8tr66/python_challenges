'''
Validate Data for Phone Numbers
https://www.reddit.com/r/dailyprogrammer/comments/pv98f/2182012_challenge_10_easy/
'''

import re


def validate_phone_number(p):
    if re.match('((\(\d{3}\)|\d{3})[- .]?)?\d{3}[- .]?\d{4}$', p) is None:
        valid = False
    else:
        valid = True

    return valid


def main():
    # Ask user for input
    user_input = input('Please input a phone number: ')

    # Calling function to validate the user input
    is_phone_number = validate_phone_number(user_input)

    # Printing result
    if is_phone_number is True:
        print('The number entered is a valid phone number.')
    else:
        print('The number entered is not a valid phone number.')


if __name__ == "__main__":
    main()
