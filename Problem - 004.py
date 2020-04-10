def next_lower_palindrome():
    """
    Product of largest three digit numbers is 999*999 = 998001 (6 digits).
    The next lower 6 digit palindrome will be 997799, then 996699, 995599, .... 989989, 988889, 987789, and so on.
    Product of smallest three digit numbers is 100*100 = 10000 (5 digits).
    After exhausting all six digit palindromes, the pattern will be 99999, 99899, .... 98989, 98889, 98789, and so on.
    """
    for i in range(997, 99, -1):
        yield int(str(i) + str(i)[::-1])

    for i in range(99, 9, -1):
        for j in range(9, -1, -1):
            yield int(str(i) + str(j) + str(i)[::-1])


def is_three_digits_product(n):
    for i in range(100, 1000):
        if not n % i:
            if 99 < n // i < 1000:
                return True
    return False


for i in next_lower_palindrome():
    if is_three_digits_product(i):
        print(i)
        break
