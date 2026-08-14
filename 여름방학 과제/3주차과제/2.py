x, y = map(int, input().split())
sX, sY = map(int, input().split())
move = input()

for i in move:
	if i == 'U':
		if sX > 1:
			sX -= 1
			
	elif i == 'D':
		if sX < x:
			sX += 1
			
	elif i == 'L':
		if sY > 1:
			sY -= 1
			
	elif i == 'R':
		if sY < y:
			sY += 1

print(sX, sY)