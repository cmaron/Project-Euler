n = 2520
found = 0
while found < 20:
	found = 0
	for i in range(20,0,-1):
		if n%i == 0:
			found += 1
		else:
			break
	n += 20

print n-20