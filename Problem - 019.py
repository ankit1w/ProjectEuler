days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def is_leap_year(year):
	return (not year % 4 and year % 100) or not year % 400


count = 0
days_since = 0
for i in range(1900, 2001):
	for j in range(1, 13):

		if days_since % 7 == 6 and i != 1900:
			count += 1

		days_since += days_in_month[j]
		if j == 2 and is_leap_year(i):
			days_since += 1

print(count)
