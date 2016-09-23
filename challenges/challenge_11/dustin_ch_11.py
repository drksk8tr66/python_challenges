import datetime


def convert(d, m, y):
    if len([x for x in [d, m, y] if str(x).isnumeric() == True]) != 3:
        return "Invalid Date"
    try:
        return datetime.date(y, m, d).strftime('%A')
    except ValueError:
        return "Invalid Date"


def convert_golf(d, m, y):
    try:
        return datetime.date(y, m, d).strftime('%A')
    except (ValueError, TypeError):
        return "Invalid Date"


if __name__ == '__main__':
    d = 31
    m = 12
    y = 9999
    print(convert(d, m, y))
    print(convert_golf(d, m, y))
