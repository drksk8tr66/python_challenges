import random
import string
import os

oneFile = open('‪Numbers.txt', 'w')
# userInput = input('How many passwords do you want?')


def get_pwd():
    a = input('How many passwords do you want?')
    while not a.isdigit():
        if a.isalpha() or a.isalnum():
            print('Input not valid. Please enter a number.')
            a = input('How many passwords do you want?')
    return a


def get_len():
    len = input('How many characters would you like the passwords to be?')
    while not len.isdigit() or int(len) < 8:
        print('Input not valid. Please enter a number greater than 7 for stronger passwords.')
        len = input('How many characters would you like the passwords to be?')
    return len


userInput = get_pwd()
length = get_len()
key_count = 0
value_count = 0

while length.isdigit() and int(length) > 7:
    for userInput in range(int(userInput)):
        while key_count <= userInput:
            key_count += 1
            text = ''.join([random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits +
                                          string.punctuation) for n in range(int(length))])
            oneFile.write(text + "\n")
    oneFile.close()
    break

print("Your passwords are saved in a text file in " + os.getcwd())
