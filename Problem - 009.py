for a in range(1, 1000):
	for b in range(a + 1, 1000):
		c = 1000 - a - b
		if c in range(1000) and c == (a * a + b * b) ** 0.5:
			print(a * b * c)
