from CommonAlgorithms import factor


def next_triangle_number():
    term = 1
    num = 1
    while True:
        yield num
        term += 1
        num += term


for i in next_triangle_number():
    if factor.count_factors(i) > 500:
        print(i)
        break
