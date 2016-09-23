from datetime import datetime

def getweekday(m, d, y):
    try:
        wkday = datetime(int(y), int(m), int(d)).weekday()
    except ValueError:
        print("Invalid Date")
    else:
        wkdaylist = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        print(wkdaylist[wkday])

