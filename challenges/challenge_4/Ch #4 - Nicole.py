'''
Random Password Generator
https://www.reddit.com/r/dailyprogrammer/comments/pm6oj/2122012_challenge_4_easy/
'''

import random


def generate_password():
    # Finding out how many characters the user wants the password to be
    num_chars = 'unknown'
    while not str(num_chars).isnumeric() or int(num_chars) < 8:
        num_chars = input('How many characters would you like the password to be? ')
        if num_chars in ('Q', 'q'):
            exit()
        if not num_chars.isnumeric():
            print('Valid number not entered.')
        if num_chars.isnumeric() and int(num_chars) < 8:
            print('Strong passwords are at least 8 characters in length.')

    # Generating four random numbers based on the number of characters
    # This will ensure that we have at least two of each type (upper, lower, number, symbol)
    rand1 = random.randint(2, int(num_chars) - 6)
    rand2 = random.randint(2, int(num_chars) - rand1 - 4)
    rand3 = random.randint(2, int(num_chars) - (rand1 + rand2) - 2)
    rand4 = int(num_chars) - (rand1 + rand2 + rand3)

    # Strings containing the upper case, lower case, numbers, and symbols to be used in passwords
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    number = '1234567890'
    symbol = '!@#$%^&*()'

    # Randomly picking characters, numbers, and symbols from each of the strings
    password = ''.join(random.sample(random.sample(upper, rand1) + random.sample(lower, rand2)
                                     + random.sample(number, rand3) + random.sample(symbol, rand4), int(num_chars)))

    # Returning the password
    return password


def main():
    print('Enter Q at any time to exit the program.\n')

    # Finding out how many passwords the user wants to generate
    num_passwords = 'unknown'
    while not num_passwords.isnumeric():
        num_passwords = input('How many passwords would you like to generate? ')
        if num_passwords in ('Q', 'q'):
            exit()
        if not num_passwords.isnumeric():
            print('Valid number not entered.')

    # Calling the generate function password and displaying the results
    for i in range(0, int(num_passwords)):
        print('Password: ' + generate_password())


if __name__ == "__main__":
    main()
