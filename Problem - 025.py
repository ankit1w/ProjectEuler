index = 1
x, y = 1, 1
while True:
	if len(str(x)) == 1000:
		break
	x, y = y, x + y
	index += 1

print(index)
