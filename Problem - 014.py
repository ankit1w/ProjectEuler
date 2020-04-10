def update_chain(n):
    count = 0
    num = n

    while True:
        if n in chain_length:
            count += chain_length[n]
            break
        if not n % 2:
            n /= 2
        else:
            n = 3 * n + 1
        count += 1

    chain_length[num] = count


longest_chain = (0, 0)
chain_length = {1: 1}

for i in range(1, 1000000):
    update_chain(i)
    if chain_length[i] > longest_chain[0]:
        longest_chain = (chain_length[i], i)

print(longest_chain[1])
