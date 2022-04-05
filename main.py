import calendar

print(calendar.weekheader(3))


print(calendar.firstweekday())

print(calendar.month(2022,4))

print(calendar.monthcalendar(2022,4))

print(calendar.calendar(2022))

day_of_the_week =calendar.weekday(2022,4,5)
print(day_of_the_week)

is_leap =calendar.isleap(2022)
print(is_leap)

how_many_leap_days =calendar.leapdays(2000, 2022)
print(how_many_leap_days)
