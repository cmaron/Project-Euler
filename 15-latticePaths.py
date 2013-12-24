def fact(n):
	return reduce(lambda x,y: x*y, range(n,0,-1))

n = 20 + 20
k = 20

n_c_k = fact(n)/( fact(n-k) * fact(k) )

print n_c_k

# Interesting notion from the comments on the problem:
#################################################################################
# Check this out! The answer is the sum of the answers above and behind         #
# the desired position in the grid!                                             #
#                                                                               #
#     1   1   1   1   1                                                         #
#     +---+---+---+---+                                                         #
#   1 | 2,| 3,| 4,| 5,|           ----( 15 )                                    #
#     +---+---+---+---+           |      |                                      #
#   1 | 3,| 6,|10,|15,|           V      |                                      #
#     +---+---+---+---+          ( 15 )  |                                      #
#   1 | 4,|10,|20,|35,|       -->(+20 )  |                                      #
#     +---+---+---+---+       |          |                                      #
#   1 | 5,|15,|35,|70,|  ( 20 )-------(=35 )                                    #
#     +---+---+---+---+                                                         #
#################################################################################