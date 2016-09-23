from datetime import datetime

def getweekday(d, m, y):
    try:
        wkday = datetime(int(y), int(m), int(d)).weekday()
    except ValueError:
        return "Invalid Date"
    else:
        wkdaylist = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return wkdaylist[wkday]


print(getweekday(23, 9, 2016))

