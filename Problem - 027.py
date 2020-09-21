from CommonAlgorithms import prime

n = 0
while True:
	for a in range(-999, 1000):
		for b in range(-1000, 1001):
			n = 0
				if (val := n*n + a*n + b) > 2:
					if prime.is_prime(val):
						n += 1
						break
				else:
					break
