from CommonAlgorithms import prime


count = 0
num = 1
while count < 10001:
    num += 1
    if prime.is_prime(num):
        count += 1

print(num)
