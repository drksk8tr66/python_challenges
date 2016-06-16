
# https://www.reddit.com/r/dailyprogrammer/comments/pih8x/easy_challenge_1/

name = str(input("What is your name? "))
age = str(input("How old are you? "))
username = str(input("What is your username? "))
info = [name, age, username]

print("Your name is %s, you are %s years old, and your username is %s" % (name, age, username))

# Bonus points
f = open("Ch #1 - Dustin.txt", 'w', newline='')
for x in info:
    f.write(x + '\n')
f.close()





