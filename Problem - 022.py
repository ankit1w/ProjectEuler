from string import ascii_uppercase as uc

from urllib.request import urlopen

name_data = urlopen('https://projecteuler.net/project/resources/p022_names.txt').read().decode()

names = sorted(eval('[' + name_data + ']'))

total_score = 0
for i, name in enumerate(names):
	total_score += (i + 1) * sum(uc.index(i) + 1 for i in name)

print(total_score)
