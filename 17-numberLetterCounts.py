number_words = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven',
8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen',
15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',
40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety', 100:'one hundred',
1000:'one thousand'}


def get_word(n):
	if n in number_words:
		return number_words[n]
	if n > 20 and n < 100:
		ones = int(round(n/10))
		power = ones*10
		return get_word(power) + ' ' + get_word(n-power)
	if n >= 100 and n < 1000:
		ones = int(round(n/100))
		tens = int(round(n/10))-10
		tens_power = tens*10
		if n % 100 == 0:
			return get_word(ones) + ' hundred'
		else:
			#print ones, tens, tens_power, n - (ones*100), get_word(ones) + ' hundred and ' + get_word(n - (ones*100))
			return get_word(ones) + ' hundred and ' + get_word(n - (ones*100))
		
	return 'Unknown'

words = ''
for i in range(1,1001):
	words += get_word(i)
	
print len(words.replace(' ',''))
