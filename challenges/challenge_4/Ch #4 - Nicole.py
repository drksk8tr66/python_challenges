'''
Random Password Generator
https://www.reddit.com/r/dailyprogrammer/comments/pm6oj/2122012_challenge_4_easy/
'''

import random


def generate_password():
    # Finding out how many characters the user wants the password to be
    num_chars = 'unknown'
    while not num_chars.isnumeric():
        num_chars = input('How many characters would you like the password to be? ')
        if num_chars in ('Q', 'q'):
            exit()
        if not num_chars.isnumeric():
            print('Valid number not entered')

    # Generating four random numbers based on the number of characters
    # This will ensure that we have at least one upper case, lower case, number, and symbol
    rand1 = random.randint(1, int(num_chars) - 3)
    rand2 = random.randint(1, int(num_chars) - rand1 - 2)
    rand3 = random.randint(1, int(num_chars) - (rand1 + rand2) - 1)
    rand4 = int(num_chars) - (rand1 + rand2 + rand3)

    # Strings containing the upper case, lower case, numbers, and symbols to be used in passwords
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    number = '1234567890'
    symbol = '!@#$%^&*()'

    # Randomly picking characters, numbers, and symbols from each of the strings
    part1 = ''.join(random.choice(upper) for i in range(0, rand1))
    part2 = ''.join(random.choice(lower) for i in range(0, rand2))
    part3 = ''.join(random.choice(number) for i in range(0, rand3))
    part4 = ''.join(random.choice(symbol) for i in range(0, rand4))

    # Shuffling the results and returning the password
    return ''.join(''.join(random.sample(part1 + part2 + part3 + part4, int(num_chars))))


def main():
    print('Press Q at any time to exit the program.\n')

    # Finding out how many passwords the user wants to generate
    num_passwords = 'unknown'
    while not num_passwords.isnumeric():
        num_passwords = input('How many passwords would you like to generate? ')
        if num_passwords in ('Q', 'q'):
            exit()
        if not num_passwords.isnumeric():
            print('Valid number not entered')

    # Calling the generate function password and displaying the results
    for i in range(0, int(num_passwords)):
        print(generate_password())


if __name__ == "__main__":
    main()
