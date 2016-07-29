'''
Print Same Line
https://www.reddit.com/r/dailyprogrammer/comments/pserp/2162012_challenge_8_easy/
'''


def main():
    # Loop through each number of bottles
    for i in range(1, 100):
        # Number of bottles
        bottles = 100 - i
        next_bottles = bottles - 1
        end = ", "

        # Being gramatically correct
        if bottles == 1:
            bottles_word = 'bottle'
        else:
            bottles_word = 'bottles'
        if next_bottles == 1:
            next_bottles_word = 'bottle'
        else:
            next_bottles_word = 'bottles'
        if next_bottles == 0:
            next_bottles = 'no more'
            end = ""

        # Print to screen
        print('{0} {1} of beer on the wall, {0} {1} of beer, take one down and pass it around, {2} {3} of '
              'beer on the wall'.format(bottles, bottles_word, next_bottles, next_bottles_word),
              end=end)


if __name__ == "__main__":
    main()
