from CommonAlgorithms import factor, prime

num = 600851475143

for factor in sorted(factor.factors_of(num), reverse=True):
    if prime.is_prime(factor):
        print(factor)
        break
