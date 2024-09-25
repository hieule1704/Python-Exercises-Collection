def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def next_day(date, month, year):
    month_31 = [1, 3, 5, 7, 8, 10, 12]
    month_30 = [4, 6, 9, 11]

    if month in month_31:
        max_days = 31
    elif month in month_30:
        max_days = 30
    else:
        max_days = 29 if is_leap_year(year) else 28

    date += 1
    if date > max_days:
        date = 1
        month += 1
        if month > 12:
            month = 1
            year += 1

    return date, month, year


date = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

date, month, year = next_day(date, month, year)
print(f"The next day is {date}/{month}/{year}")
