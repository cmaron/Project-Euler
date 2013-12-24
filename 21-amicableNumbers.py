import pprint

def sum_divisors(n):
    x = 0
    i = 1 
    while(i < n):
        if(n % i == 0):
            x += i
        i += 1
    return x

amicable_numbers = {}

for i in range(0,10001):
	sum_d = sum_divisors(i)
	if sum_d > 0:
		other_sum = sum_divisors(sum_d)
		sum_other_sum = sum_divisors(other_sum)
		print i, sum_d, other_sum, sum_other_sum,
		if i != sum_d and i == other_sum and sum_other_sum == sum_d:
			amicable_numbers.setdefault(i,True)
			amicable_numbers.setdefault(sum_d,True)

print sum(amicable_numbers.keys())
