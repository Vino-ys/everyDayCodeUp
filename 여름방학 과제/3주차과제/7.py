n = int(input())
stack = []
list = []

for _ in range(n):
	list.append(input().split())

for i in list:
	commend = i[0]
	
	if commend == 'PUSH':
		stack.append(i[1])
		
	elif commend == 'SIZE':
		print(len(stack))
		
	elif commend == 'POP':
		print(stack.pop())