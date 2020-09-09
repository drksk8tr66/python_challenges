
def get_name():
    while True:
        n = input("What is your name?")
        if n.isalpha():
            break
        print("That doesn't seem like a name. Please enter your name.")
    return n


def get_age():
    while True:
        a = input("How old are you?")
        if a.isdigit():
            break
        print("That doesn't seem like a number. Please enter your age.")
    return a


def get_user():
    while True:
        u = input("What is your username?")
        if sum(c.isalpha() for c in u) == 4 and sum(c.isdigit() for c in u) == 4:
         print("That doesn't seem like a username. Please enter your username.")
    return u


name = get_name()
age = get_age()
user = get_user()


print("Your name is %s, you are %s years old, your username is %s." % (name, age, user))

f = open('Ch #1 - Addie.txt', 'w')
f.write("Your name is %s, you are %s years old, your username is %s." % (name, age, user))
