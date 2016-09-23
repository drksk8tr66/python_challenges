
from datetime import datetime


def getweekday(m, d, y):
    dtedict = {'month': m, 'day': d, 'year': y}
    mrange = list(range(1, 13))
    drange = list(range(1, 32))
    yrange = list(range(1900, 2300))

    for i in dtedict.values():
        try:
           for ii in dtedict.values():
               int(ii)
        except ValueError:
            print("Dude. The inputs must be integers.")
            return True
        else:
            if int(dtedict["month"]) not in mrange:
                print("Invalid Month Entered. Must be 1 to 12. TRY AGAIN. You entered: ", dtedict)
                return True
            elif int(dtedict["day"]) not in drange:
                print("Invalid Day Entered. Must be 1 to 31. TRY AGAIN. You entered: ", dtedict)
                return True
            elif int(dtedict["year"]) not in yrange:
                print("The year you entered is out of range. Must be between 1900 and 2300. TRY AGAIN. You entered: ", dtedict)
                return True
            else:
                prelimdate = datetime(int(y), int(m), int(d))
                wkday = prelimdate.weekday()
                wkdaylist = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
                print(wkdaylist[wkday])
                return False

def main():
    oloop = True
    while oloop:
        print()
        m = input("Enter the month in integer format, or Q to END:")
        d = input("Enter the day in integer format, or Q to END:")
        y = input("Enter the year in integer format, or Q to END:")
        ex = [m, d, y]
        if "q" in [l.lower() for l in ex]:
            print("END")
            break
        oloop = getweekday(m, d, y)


if __name__ == "__main__":
    main()


