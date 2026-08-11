one = 0
two = 0
three = 0
four = 0
whkvy = 0

n = int(input())
for i in range(n):
	x, y = map(int, input().split())
	if x > 0:
		if y > 0:
			one += 1
		elif y < 0:
			four += 1
		else:
			whkvy += 1
	elif x < 0:
		if y > 0:
			two += 1
		elif y < 0:
			three += 1
		else:
			whkvy += 1
	else:
		whkvy += 1

print(one, two, three, four, whkvy)