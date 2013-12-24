def sum_divisors(n):
    x = 0
    i = 1 
    while(i < n):
        if(n % i == 0):
            x += i
        i += 1
    return x
    
def is_abundant(n):
	return sum_divisors(n)>n
	
abundants = []
for i in range(11,28124):
	if is_abundant(i):
		abundants.append(i)

sum_of_abundants = {}
for i in range(len(abundants)):
	for j in range(i,len(abundants)):
		if abundants[i] + abundants[j] <= 28123:
			sum_of_abundants[abundants[i] + abundants[j]] = True
		else:
			break

print sum(set(range(0,28124)) - set(sum_of_abundants.keys()))