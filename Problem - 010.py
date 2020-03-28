def get_primes(n):
    """
    Sieve of Eratosthenes
    """
    prime = [True] * (n + 1)
    i = 2
    while i * i <= n:
        if prime[i]:
            for j in range(i * 2, n + 1, i):
                prime[j] = False
        i += 1

    return filter(lambda x: prime[x], range(2, n + 1))


print(sum(get_primes(2000000)))
