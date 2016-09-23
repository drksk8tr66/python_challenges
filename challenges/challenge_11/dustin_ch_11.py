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
    a = 31
    b = 12
    c = 9999
    print(convert(a, b, c))
    print(convert_golf(a, b, c))
