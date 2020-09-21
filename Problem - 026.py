max_recur, num = 0, 0

for d in range(2, 1000):
	val = 1
	remainders = [1]

	while True:
		val *= 10
		while val < d:
			val = val * 10
			remainders.append(0)

		val %= d

		if not val:
			break
		if val in remainders:
			if (count := len(remainders) - remainders.index(val)) > max_recur:
				max_recur = count
				num = d
			break
		remainders.append(val)

print(num)
