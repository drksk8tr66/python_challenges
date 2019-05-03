#!/usr/bin/env python3
"""
create a program that will ask the users name, age, and username. have it tell
them the information back, in the format:
your name is (blank), you are (blank) years old, and your username is (blank)
for extra credit, have the program log this information in a file to be
accessed later.
"""
from string import Template
from pathlib import Path

def challenge1():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    username = input("Enter your username: ")

    return Template("Your name is $name, you are $age years old,"
                   "and your username is $username.\n").safe_substitute(locals())

def do_output(string_to_use):
    print(string_to_use)
    Path('./Ryan.txt').write_text(challenge_output)

if __name__ == '__main__':
    challenge_output = challenge1()
    do_output(challenge_output)
