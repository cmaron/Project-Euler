palendromes = {}
for i in range(999,100,-1):
	for j in range(999,100,-1):
		n = str(i*j)
		if len(n)%2==0:
			m = len(n)/2
			if n[:m] == n[m:][::-1]:
				if not n in palendromes:
					palendromes[n] = []
				palendromes[n].append((i,j))
				
import pprint
pprint.pprint(palendromes)
