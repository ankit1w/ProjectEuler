from CommonAlgorithms import factor

abundant_data = dict()


def is_abundant(n):
	if n in abundant_data:
		return abundant_data[n]
	abundant_data[n] = sum(factor.factors_of(n)) - n > n
	return abundant_data[n]


total_sum = 0
for i in range(1, 28123):
	abundant = False
	for j in range(1, i // 2 + 1):
		if is_abundant(j) and is_abundant(i - j):
			abundant = True
			break
	if not abundant:
		total_sum += i

print(total_sum)
