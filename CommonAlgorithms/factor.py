def factors_of(n):
    for i in range(1, int(n ** .5) + 1):
        if not n % i:
            yield i
            if n / i != i:
                yield n // i


def count_factors(n):
    count = 0
    for i in range(1, int(n ** .5) + 1):
        if not n % i:
            count += 1
            if n / i != i:
                count += 1
    return count
