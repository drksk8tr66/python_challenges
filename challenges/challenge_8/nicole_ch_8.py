'''
Sorting
https://www.reddit.com/r/dailyprogrammer/comments/pu1rf/2172012_challenge_9_easy/
'''


def sort_list(values):
    # Determining if the value is a number or a string
    num_values = []
    str_values = []
    for v in values:
        if v.isnumeric():
            num_values.append(v)
        else:
            str_values.append(v)

    # Sorting the values accordingly
    num_values = sorted(num_values, key=float)
    str_values = sorted(str_values)
    values = num_values + str_values

    return values


def main():
    # List to store values in
    values = []

    # Ask user for values
    print('Please enter the values you would like to sort.  Press the enter key between each value.  '
          'Enter a blank line when finished.')
    while True:
        i = input()
        if not i:
            break
        values.append(i)

    # Calling function to sort the values
    values = sort_list(values)

    # Printing the sorted values to screen
    print('Sorted values:')
    print(*values, sep='\n')


if __name__ == "__main__":
    main()
