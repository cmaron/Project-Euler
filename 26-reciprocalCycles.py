# http://mathworld.wolfram.com/DecimalExpansion.html
# http://stackoverflow.com/questions/1315595/algorithm-for-detecting-repeating-decimals
# http://stackoverflow.com/questions/12098461/how-can-i-detect-if-a-float-has-a-repeating-decimal-expansion-in-c

# Adapted from http://www.nerdparadise.com/tech/python/repeatingdecimaldivision/
def find_repeating(d):
	v = 1 // d
	n = 10 * (1 - v * d)
	a = str(v)
	a += '.'
	
	# Maintain a list of all the intermediate ns 
	# and the length of the output at the point where that 
	# n was encountered. If you encounter the same 
	# n again, then the decimal repeats itself from 
	# the last index that n was encountered at. 
	seen_ns = {}
	
	while n > 0:
		
		existing_n = seen_ns.get(n, None)
		if existing_n != None:
			start_repeat_index = existing_n
			return a[start_repeat_index:]
		seen_ns[n] = len(a)
		
		v = n // d
		a += str(v)
		n -= v * d
		n *= 10
	
	return ''

max = [0,'', 0]
for i in range(2,1001):
	n = find_repeating(i)
	if len(n) > max[2]:
		max = [i,n, len(n)]

print max

#######
# Wow #
#######

# I took an approach to this based on the following observations (which I discovered on Wikipedia):
# 
# Observation 1: Any denominator divisible by 2 or 5 does not produce a repeating decimal.  All others do.
# Observation 2: There are the following cases for repeating decimals...
# 
# A) Prime denominators p (other than 2 or 5)
# 
#    i.  If 10 is a primitive root modulo p, the period is equal to p−1.
# 
#    ii. If not, the period is equal to a prime factor of p−1. 
# 
# B) Reciprocals of composite integers coprime to 10 
# 
#    i.  The period of 1p2 is equal to λ(p2) where p is a prime other than 2 or 5 and λ(n) is the Carmichael function.
# 
#    ii. The period of 1pq equals LCM(λ(p),λ(q)) where p and q are primes other than 2 and 5.
# 
#    iii. If p, q, r, etc. are primes other than 2 or 5, and k, ℓ, m, etc. are positive integers then 1pkqℓrm… is a repeating decimal with a period of LCM(Tpk,Tqℓ,Trm,…) where Tpk,Tqℓ,Trm, etc. are respectively the periods of the repeating decimals 1pk, 1qℓ, 1rm, etc. as defined above.
# 
# C) Reciprocals of integers not coprime to 10
# 
#    i. This is of the form 12a5bpkqℓ… which has an initial transient of max(a,b) digits and then a subsequent repeatend which is the same as 1pkqℓ…
# 
# Of the cases in Obs. 2, only Ai was relevant, since C reduces to cases A or B, case Biii reduces the cases above it, and the output of λ(n) cannot exceed n−1 nor can the output for all non-prime n between primes pi and pi+1 exceed pi.  Hence, you only have to find the greatest prime p such that 10 is a primitive root modulo p.
# 
# If you wanted to make the implementation more efficient you could try to find the closest prime to 1000 by counting down instead.
# 
# import math
# 
# def is_prime(num):
#   """Return True if `num' is prime and False otherwise."""
#   for n in range(2,int(math.sqrt(num))+1):
#     if num % n == 0:
#       return False
#   return True
# 
# def primitive_root(b,p):
#   """Return True if b is a primitive root (modulo p), False otherwise."""
#   return set([b**r % p for r in range(1,p)]) == set(range(1,p))
# 
# print max([p for p in range(2,1001) if is_prime(p) and primitive_root(10,p)])