n = int(input())
list = []
s = []

for _ in range(n):
	list.append(input().split())

for i in range(n):
	commend = list[i]
	if commend[0] == 'TYPE':
		s.append(commend[1])
	elif commend[0] == 'UNDO':
		s.pop()

if len(s) == 0:
	print('EMPTY')
else:
	for i in s:
		print(i, end = "")