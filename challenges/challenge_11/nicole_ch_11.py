'''
Given Date, Get Day of Week
https://www.reddit.com/r/dailyprogrammer/comments/pwons/2192012_challenge_11_easy/
'''

import calendar


def get_day_of_week(d, m, y):
    try:
        return calendar.day_name[calendar.weekday(y, m, d)]
    except (ValueError, TypeError):
        return "Invalid Date"


def main():
    # Declaring variables
    day = ''
    month = ''
    year = ''

    # Asking user for input
    print('This program will output the day of week for an entered date.')
    while day.isdigit() is False:
        day = input('Please input a day (as an integer): ')
    while month.isdigit() is False:
        month = input('Please input a month (as an integer): ')
    while year.isdigit() is False:
        year = input('Please input a year (as an integer): ')

    # Calling function to get day of week and displaying to user
    print(get_day_of_week(int(day), int(month), int(year)))


if __name__ == "__main__":
    main()
