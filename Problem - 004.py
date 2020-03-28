def next_lower_palindrome():
    """
    Product of largest three digit numbers is 999*999 = 998001 (6 digits).
    Product of smallest three digit numbers is 100*100 = 10000 (5 digits).
    The next lower 6 digit palindrome will be 997799, then 996699, 995599, .... 989989, 988889, 987789, and so on.
    After exhausting all six digit palindromes, the pattern will be 99999, 99899, .... 98989, 98889, 98789, and so on.
    """
    for i in range(997, 99, -1):
        yield int(str(i) + str(i)[::-1])

    for i in range(99, 9, -1):
        for j in range(9, -1, -1):
            yield int(str(i) + str(j) + str(i)[::-1])


def get_three_digit_factor(x):
    """
    Get a number and return the factors only when the quotient is three digits, otherwise return False.
    The divisor ranges from 999 to 100, so it is always three digits.
    """
    divisor = 999
    while 100 <= divisor:
        if x % divisor == 0:
            quotient = x // divisor
            if len(str(quotient)) == 3:
                return divisor, quotient
        divisor -= 1

    return False


for i in next_lower_palindrome():
    if get_three_digit_factor(i):
        print(i)
        break
