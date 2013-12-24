with open('./22-names.txt') as input:
	names = sorted(map(lambda a: ''.join(list(a)[1:-1]), input.read().split(',')))
	
	overall = 0
	for i in range(len(names)):
		overall += reduce(lambda x,y: x+y, map(lambda z: ord(z)-64, list(names[i])))*(i+1)
		
	print overall