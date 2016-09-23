from datetime import datetime


def getweekday(d, m, y):
    try:
        wkday = datetime(y, m, d).weekday()
    except (ValueError, TypeError):
        return "Invalid Date"
    else:
        wkdaylist = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return wkdaylist[wkday]
