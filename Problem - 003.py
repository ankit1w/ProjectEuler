def is_prime(x):
    if num % 2 == 0:
        return False
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True


def get_factors(x):
    """
    Collecting all factors in increasing order, and storing them, along with the quotients when they divide the number.
    The loop stops when the divisor has already been collected as a quotient from a previous division,
    and any further divisor will only result in repeated comparisons.
    """
    factors = list()
    divisor = 2

    while divisor not in factors:

        if x % divisor == 0:
            quotient = x // divisor
            factors.extend([divisor, quotient])
        divisor += 1

    return factors


num = 600851475143

for factor in sorted(get_factors(num), reverse=True):
    if is_prime(factor):
        print(factor)
        break
