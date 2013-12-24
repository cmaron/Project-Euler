def permutation_generator(s):
	if len(s) == 1:
		yield s
	for i in range(len(s)):
		for perm in permutation_generator(s[:i] + s[i+1:]):
			yield s[i] + perm

i = 0
for p in permutation_generator('0123456789'):
	i += 1
	print i, p
	if (i >= 1000000):
		break
