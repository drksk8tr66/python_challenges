'''
Validate Data for Phone Numbers
https://www.reddit.com/r/dailyprogrammer/comments/pv98f/2182012_challenge_10_easy/
'''

import re


def validate(t_num):
    if not t_num:
        return False
    if type(t_num) is not str:
        return False
    if re.match("[0-9]{3}-? ?[0-9]{3}-? ?[0-9]{4}$|[0-9]{3} ?[0-9]{4}$|[0-9]{3}\.?[0-9]{4}$|"
                "([0-9]{3}-)?[0-9]{3}-[0-9]{4}$|[0-9]{3}\.[0-9]{3}\.[0-9]{4}$|"
                "\([0-9]{3}\) ?[0-9]{3}-?[0-9]{4}$", t_num):
        return True
    else:
        return False


if __name__ == '__main__':
    print(validate('123:4567'))
    print(validate('(123)4567890'))
    print(validate('123.4567'))
    print(validate('123-456.7890'))
    print(validate('123.456-7890'))
    print(validate('1234567'))
    print(validate('123456-7890'))
    print(validate('123-456-7890'))
    print(validate('123.456.7890'))
    print(validate('(123)456-7890'))
    print(validate('(123) 456-7890'))
    print(validate('456-7890'))
    print(validate('123-45-6789'))
    print(validate('123:4567890'))
    print(validate('123/456-7890'))
