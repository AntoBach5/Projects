import calendar
from datetime import datetime, time, date

enter = int(input("Enter any month in number (ej.: 1 for January, 2 for February, etc.): "))

month_name = ""

if enter == 1:
    month_name = "January"
elif enter == 2:
    month_name = "February"
elif enter == 3:
    month_name = "March"
elif enter == 4:
    month_name = "April"
elif enter == 5:
    month_name = "May"
elif enter == 6:
    month_name = "June"
elif enter == 7:
    month_name = "July"
elif enter == 8:
    month_name = "August"
elif enter == 9:
    month_name = "September"
elif enter == 10:
    month_name = "October"
elif enter == 11:
    month_name = "November"
elif enter == 12:
    month_name = "December"

year = datetime.now().year

print("The month you entered is: ",month_name)
print("And here is the calendar of that month: ")
print("\n",calendar.month(year, enter))