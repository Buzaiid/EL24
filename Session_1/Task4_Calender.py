import calendar

year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))

cal = calendar.TextCalendar(calendar.SATURDAY) #month starts with SAT
#cal = calendar.TextCalendar(calendar.SUNDAY)  #month starts with SUN

formatted_month = cal.formatmonth(year, month ,0,0)

print(formatted_month)