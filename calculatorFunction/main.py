def is_leap_year(year):
    # A year is a leap year if it is divisible by 4
    # except for end-of-century years, which must be divisible by 400.
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False
year = int(input("Enter the year: "))
mont = int(input("Enter the month: "))
month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}
if is_leap_year(year):
    month[2] = 29

def hi(year, mont,month):
    print("The month is", month[mont])
hi(year, mont,month)





