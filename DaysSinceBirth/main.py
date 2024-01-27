"""
Given your birthday and the current date, calculate your age in days. Compensate for leap days. Assume that the
birthday and the current date are correct dates. If you were born 1 Jan 2012 and today's date is 2 Jan 2012, you are
1 day old.
"""
from datetime import datetime


def is_leap_year(year):
    leap_year = False

    if year % 4 == 0:
        leap_year = True
        if year % 100 == 0 and year % 400 == 0:
            leap_year = True
    return leap_year


def days_between_dates(y1, m1, d1, y2, m2, d2):
    days_in_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    days = days_in_month[m1 - 1] - d1
    m1 += 1

    while not (y1 == y2 and m1 == m2):
        if m1 > 12:
            m1 = 1
            y1 += 1
        else:
            days += days_in_month[m1 - 1]
            m1 += 1

    days += d2

    while y1 < y2:
        y1 += 1
        if is_leap_year(y1):
            days += 366
        else:
            days += 365
    return days


def next_day(year, month, day):
    pass


def built_in_days_between_dates(date1_str, date2_str):
    # Convert date strings to datetime objects
    date1 = datetime.strptime(date1_str, "%Y-%m-%d")
    date2 = datetime.strptime(date2_str, "%Y-%m-%d")

    # Calculate the difference between the two dates
    delta = date2 - date1

    # Return the number of days as an integer
    return abs(delta.days + 1)  # include end day


def main():
    print(f"It's been {days_between_dates(1973, 9, 1, 2024, 1, 20)} days since you were born")
    print(f"It's been {built_in_days_between_dates('1973-09-01', '2024-01-20')} days since you were born")
    print(days_between_dates(1973, 9, 1, 1980, 9, 1))


if __name__ == '__main__':
    main()
