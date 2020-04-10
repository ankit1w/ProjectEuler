def is_prime(n):
    assert n > 1, "Prime numbers start from 2."

    if n == 2:
        return True

    elif not n % 2:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if not n % i:
            return False

    return True


def primes_below(n):
    """
    Sieve of Eratosthenes
    """
    assert n > 1, "Prime numbers start from 2."

    prime = [True] * n
    i = 2
    while i * i <= n:
        if prime[i]:
            for j in range(i * 2, n, i):
                prime[j] = False
        i += 1

    return filter(lambda x: prime[x], range(2, n))
