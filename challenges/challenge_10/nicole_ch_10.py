'''
Validate Data for Phone Numbers
https://www.reddit.com/r/dailyprogrammer/comments/pv98f/2182012_challenge_10_easy/
'''

import re


def validate_phone_number(p):
    only_numbers = '\d{3}?\d{3}\d{4}$'
    with_parens = '\(\d{3}\)[ ]?\d{3}[- .]?\d{4}$'
    with_spaces = '(\d{3}[ ]?)?\d{3}[ ]\d{4}$'
    with_dots = '(\d{3}[.]?)?\d{3}[.]?\d{4}$'
    with_hyphens = '(\d{3}[-]?)?\d{3}[-]?\d{4}$'

    if re.match(only_numbers, p) is not None:
        return True
    elif re.match(with_parens, p) is not None:
        return True
    elif re.match(with_spaces, p) is not None:
        return True
    elif re.match(with_dots, p) is not None:
        return True
    elif re.match(with_hyphens, p) is not None:
        return True
    else:
        return False


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
