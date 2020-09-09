# https://www.reddit.com/r/dailyprogrammer/comments/pjbj8/easy_challenge_2/

"""
Hello, coders! An important part of programming is being able to apply your programs, so your challenge for today is to
create a calculator application that has use in your life. It might be an interest calculator, or it might be something
that you can use in the classroom. For example, if you were in physics class, you might want to make a F = M * A calc.

EXTRA CREDIT: make the calculator have multiple functions! Not only should it be able to calculate F = M * A,
but also A = F/M, and M = F/A!
"""


def forcecalc(f: int = 0, m: int = 0, a: int = 0):
    if f == 0:
        return m * a
    elif m == 0:
        return f / a
    else:
        return f / m


force = 0
mass = 0
acc = 0

while sum([force, mass, acc]) == 0:
    force = int(input("How much force?"))
    mass = int(input("How much mass?"))
    acc = int(input("How much acceleration?"))

ans = forcecalc(force, mass, acc)
print(ans)
