from CommonAlgorithms import factor

amicables = set()


def d(n):
	return sum(factor.factors_of(n)) - n


for a in range(1, 10000):
	if (b := d(a)) < 10000:
		if a != b and d(b) == a:
			amicables.update((a, b))

print(sum(amicables))
