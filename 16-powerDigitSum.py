import math
import re

n = '%1.0f' % math.pow(2L,1000L)

print reduce(lambda x,y: int(x)+int(y), filter(lambda x: x != '', re.split('(\d)',n)))

# also 

print(sum(map(int, str(2 ** 1000))))