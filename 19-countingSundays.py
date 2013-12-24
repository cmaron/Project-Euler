days_in_month = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

x = 0
# M = 0, T = 1, W = 2, R = 3, F = 4, S = 5, U = 6
day_of_week = 0
month = 1
day = 1
year = 1900
d_i_m = days_in_month[month]

# This could probably be sped up by jumping a head a week/month at a time and adjusting as
# needed.
while year < 2001:
	if year > 1900 and day_of_week == 6 and day == 1:
		x += 1
	day += 1
	day_of_week += 1
	if day > d_i_m:
		day = 1
		month += 1
		if month > 12:
			month = 1
			year += 1
		d_i_m = days_in_month[month]
		if month == 2:
			if year%100 == 0:
				if year%400 == 0:
					d_i_m += 1
			elif year%4 == 0:
				d_i_m += 1
	if day_of_week > 6:
		day_of_week = 0
	print day_of_week, day, month, '/', d_i_m, year, (year > 1900 and day_of_week == 6 and day == 1)
print x


# def is_leap_year(y):
#     if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
#         return True
#     return False 
# 
# numdays = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
# 
# year, month, wday = 1901, 1, 2
# cnt = 0 
# 
# while year < 2001:
#     if wday == 0:
#         cnt += 1
# 
#     days = 29 if month == 2 and is_leap_year(year) else numdays[month-1]
#     wday = (wday + days) % 7 
# 
#     month += 1
# 
#     if month > 12: 
#         year += 1
#         month = 1 
# 
# print cnt
