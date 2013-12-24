import math

def calculate_num_divisors(n):
    count = 2
    i = 2 
    while(i**2 <= n):
        if(n % i == 0):
            count += 2
        i += 1
    return count  

i = 10
length = 0
while length < 500:
	n = (i * (i+1)) / 2
	length = calculate_num_divisors(n)
	i += 1
print n
