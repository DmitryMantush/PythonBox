import calendar
import datetime

date = input()
d, m, y = map(int, date.split('.'))
print(calendar.day_name[calendar.weekday(y, m, d)])

day = input()

z = datetime.datetime.now()
Y = z.year
M = z.month
p = calendar.day_name[calendar.weekday(Y, M, 1)]
while day != p:
    M -= 1
    if M == 0:
        Y -= 1
        M = 12
    p = calendar.day_name[calendar.weekday(Y, M, 1)]
print(M, Y)

