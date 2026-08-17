s = input()
open = 0
isGood = True

if s[0] == ')':
	isGood = False
	
for i in s:
	if i == '(':
		open += 1
	elif i == ')':
		open -= 1

if open != 0:
	isGood = False

if isGood == True:
	print('YES')
else:
	print('NO')