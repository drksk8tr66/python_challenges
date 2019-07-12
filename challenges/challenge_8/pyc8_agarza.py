def ask_list():
    str_received = input('Please enter a list.  Please remember to separate each item with a comma.\n')
    while True:
        if str_received.find(',') > -1:
            list_received = str_received.split(',')
            list_received = [x.strip() for x in list_received]
            return list_received
            break
        else:
            print('Please enter a properly formatted list.')

def is_numeric(n):
    try:
        float(n)
    except ValueError: 
        return False
    return True

def sort_custom(slist):
    lst_numeric = [float(n) for n in slist if is_numeric(n)]
    lst_numeric.sort()
    lst_str = [s for s in slist if not is_numeric(s)]
    lst_str.sort()
    return lst_str + lst_numeric
    
def main():
    lst = ask_list()
    lst_sorted = sort_custom(lst)
    print(lst_sorted)

if __name__ == '__main__':
    main()