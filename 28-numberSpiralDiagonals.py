w = 1001
h = 1001

spiral = []
n = w*h
x,y = h-1,0
px,py = 0,0
dx,dy = -1, 0
for i in range(h):
	row = []
	for j in range(w):
		row.append(0)
	spiral.append(row)

while n > 0:
	spiral[y][x] = n
	n -= 1
	x = x + dx
	y = y + dy
	if x == px and y == py:
		dx = 0
		dy = 1
	elif y == h-1-py and x == px:
		dx = 1
		dy = 0
	elif x == w-1-px and y == h-1-py:
		dx = 0
		dy = -1
	elif x == w-1-px and y == py+1:
		dx = -1
		dy = 0
		px += 1
		py += 1

x = 0
for i in range(0,h):
	x += spiral[i][i]

for i in range(0,h):
	x += spiral[i][w-1-i]
	
print x-1

# See site for better algorithms