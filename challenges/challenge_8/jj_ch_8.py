def order_list(input:list = None):
    '''
    This function uses python's built in sorted algorithm to sort a list of elements.
    As reference, Python uses the timsort. It is a hybrid merge and insertion sort.
    See wikipedia for more info
    Worst Case Performance (n log n)
    :returns list: Sorted according to python's native soring functionality
    '''
    if input is None:
        return []
    return sorted(input)


if __name__ == '__main__':
    while True:
        x = input('Please enter a list. (enter Q to quit) : ')
        if x in ('q', 'Q'):
            print('Bye bye!')
            exit()
        user_list = [e for e in x.split()]
        print('Here is your input in order {}'.format(order_list(user_list)))
