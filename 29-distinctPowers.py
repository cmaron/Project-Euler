import math
ps = []

for a in range(2,101):
	for b in range(2,101):
		ps.append(math.pow(a,b))

print len(set(ps))

# Also
# print(len(set([a**b for a in range(2,101) for b in range(2,101)])))