import datetime


def convert(d, m, y):
    if len([x for x in [d, m, y] if str(x).isnumeric() == True]) != 3:
        return "Invalid Date"
    try:
        return datetime.date(y, m, d).strftime('%A')
    except ValueError:
        return "Invalid Date"


if __name__ == '__main__':
    print(convert(13, 3, 2016))
