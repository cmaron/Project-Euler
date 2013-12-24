a=3
b=4
c=5
sum = a+b+c
for a in range(3,1000):
	for b in range(a+1,1000):
		for c in range(b+1,1000):
			if a**2 + b**2 == c**2:
				sum = a+b+c
				if sum == 1000:
					print a,b,c,sum, (a*b*c)
					break
