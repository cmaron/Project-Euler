import math

def is_prime(n):
	n_sqrt = int(math.sqrt(n))+1
	i = 2
	while i < n_sqrt:
		if n%i == 0:
				return False
		i += 1
	return True
	
i=3
found_primes = 1
while found_primes < 10001:
	if is_prime(i):
		print i,
		found_primes += 1
		print found_primes
	i += 2

