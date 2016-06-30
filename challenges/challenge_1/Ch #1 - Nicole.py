'''
Ask for Info, Store in File
https://www.reddit.com/r/dailyprogrammer/comments/pih8x/easy_challenge_1/
'''


def ask_input():
    n = input('What is your name? ')
    a = input('What is your age? ')
    u = input('What is your username? ')
    print('Your name is %s, you are %s years old, and your username is %s.' % (n, a, u))
    return n, a, u


def store_file(n, a, u):
    f = open('Ch #1 - Nicole.txt', 'w')
    f.write('Your name is %s, you are %s years old, and your username is %s.' % (n, a, u))


def main():
    name, age, username = ask_input()
    store_file(name, age, username)


if __name__ == "__main__":
    main()
