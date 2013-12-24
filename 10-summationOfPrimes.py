import math

def is_prime(n):
	n_sqrt = int(math.sqrt(n))+1
	i = 2
	while i < n_sqrt:
		if n%i == 0:
			return False
		i += 1
	return True

sum = 0
n = 2
while n < 2000000:
	if is_prime(n):
		sum += n
	n += 1

print sum