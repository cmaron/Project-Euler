import math

n = 600851475143
factors = []

def is_prime(n):
	n_sqrt = int(math.sqrt(n))+1
	i = 2
	while i < n_sqrt:
		if n%i == 0:
			return False
		i += 1
	return True

while n > 2:
	i = 2
	while n%i != 0:
		i += 1
	factors.append(i)
	n = n/i

factors.reverse()
print filter(lambda x: is_prime(x), factors)[0]