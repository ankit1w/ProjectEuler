below_19 = ('',
            'one',
            'two',
            'three',
            'four',
            'five',
            'six',
            'seven',
            'eight',
            'nine',
            'ten',
            'eleven',
            'twelve',
            'thirteen',
            'fourteen',
            'fifteen',
            'sixteen',
            'seventeen',
            'eighteen',
            'nineteen')

tens = {20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety'}


def num_to_word(n):
	if n == 1000:
		return 'one thousand'

	word = ''

	if n >= 100:
		word = below_19[n // 100] + ' hundred'
		if n % 100:
			word += ' and '

	if n % 100 < 20:
		word += below_19[n % 100]
	else:
		word += tens[n % 100 - n % 10]
		if n % 10:
			word += '-' + below_19[n % 10]

	return word


count = 0
for i in range(1, 1001):
	count += len(num_to_word(i).replace(' ', '').replace('-', ''))

print(count)
