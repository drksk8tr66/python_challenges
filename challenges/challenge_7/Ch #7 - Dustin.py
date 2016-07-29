# https://www.reddit.com/r/dailyprogrammer/comments/pserp/2162012_challenge_8_easy/


def count_bottles(bottles: int=99):
    num_bottles = bottles
    stanza1 = ' bottles of beer'
    stanza2 = ' on the wall...'
    stanza3 = '\nTake one down, pass it around, '
    while num_bottles > 1:
        print('{0}{1}{2}{0}{1}{3}'.format(num_bottles, stanza1, stanza2, stanza3))
        num_bottles -= 1
        print('{0}{1}{2}'.format(num_bottles, stanza1, stanza2))
    print('{0}{1}{2}{0}{1}{3}'.format(num_bottles, ' bottle of beer', stanza2, stanza3))
    print('No more bottles of beer on the wall!')


if __name__ == '__main__':
    count_bottles()
