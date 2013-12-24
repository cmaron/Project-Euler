def collatz_generator(n):
	yield n
	while n > 1:
		if n%2 == 0:
			n = n/2
			yield n
		else:
			n = 3*n + 1
			yield n

i = 1000000
max_chain = 0
max_num = 0
while i > 1:
	n = len(list(collatz_generator(i)))
	if n > max_chain:
		max_chain = n
		max_num = i
	i -= 1

print max_num, max_chain