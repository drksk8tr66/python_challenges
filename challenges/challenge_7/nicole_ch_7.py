'''
Print Same Line
https://www.reddit.com/r/dailyprogrammer/comments/pserp/2162012_challenge_8_easy/
'''


def main():
    # Repeating parts of the song
    part_1 = ' bottles of beer'
    part_1n = ' bottle of beer'
    part_2 = ' on the wall'
    part_3 = ' take one down and pass it around'

    # Loop for everything until we get to a part with one bottle
    for i in range(99, 2, -1):
        print('{0}{1}{2}, {0}{1},{3}, {4}{1}{2}'.format(i, part_1, part_2, part_3, i - 1), end=", ")

    # Displaying one bottle so it is gramatically correct
    print('{0}{1}{2}, {0}{1},{3}, {4}{5}{2}'.format(2, part_1, part_2, part_3, 1, part_1n), end=", ")
    print('{0}{1}{2}, {0}{1},{3}, {4}{5}{2}'.format(1, part_1n, part_2, part_3, 'no more', part_1))


if __name__ == "__main__":
    main()
