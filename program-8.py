# This is program-8.py

import calendar

year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

cal = calendar.month(year, month)
print(cal)