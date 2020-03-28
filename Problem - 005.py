from fractions import Fraction


def smallest_evenly_divisible(max_num):
    """
    To make the result evenly divisible by a number,
    multiply it by the denominator left when the result is divided by that number.
    """
    result = 1

    while max_num:
        result *= Fraction(result, max_num).denominator
        max_num -= 1
    return result


print(smallest_evenly_divisible(20))
