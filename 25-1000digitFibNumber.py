from math import pow

def fib_gen():
	prev = 0
	tmp_prev = prev
	curr = 1
	i = 1
	while True:
		yield i, curr
		tmp_prev = prev
		prev = curr
		curr += tmp_prev
		i += 1
	
for i in fib_gen():
	if len(str(i[1])) >= 1000:
		print i, len(str(i[1]))
		break
