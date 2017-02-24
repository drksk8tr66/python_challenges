import os
# https://www.reddit.com/r/dailyprogrammer/comments/pih8x/easy_challenge_1/


def gather_info(name: str=None, age: str=None, username: str=None):
    while not name:
        name = str(input("What is your name? "))
    while not age:
        age = str(input("How old are you? "))
    while not username:
        username = str(input("What is your username? "))
    info = [name, age, username]
    return info


def print_info(info: list=None):
    if info is None or len(info) < 1:
        return "You have not supplied the correct type of info"
    message = "Your name is {0}, you are {1} years old, and your username is {2}".format(info[0], info[1], info[2])
    return message


def write_to_file(info):
    # Bonus points
    f = open("Ch #1 - Dustin.txt", 'w', newline='')
    for x in info:
        f.write(str(x) + '\n')
    f.close()
    return "info saved"


def read_from_file(f_name):
    # Bonus points
    if os.path.isfile(f_name):
        f = open(f_name, 'r', newline='')
        results = []
        for x in f.readlines():
            results.append(x)
        f.close()
        print(results)
        return results
    return "file not found"


def file_cleanup():
    f = "Ch #1 - Dustin.txt"
    if os.path.isfile(f):
        os.remove(f)


if __name__ == '__main__':
    inf = gather_info()
    print_info(inf)
    write_to_file(inf)
    if os.path.isfile("Ch #1 - Dustin.txt"):
        read_from_file("Ch #1 - Dustin.txt")
        file_cleanup()

