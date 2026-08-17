n = int(input())
nset = list(map(int, input().split()))
q = int(input())
qList = list(map(int, input().split()))

result = []

for i in qList:
	if i in nset:
		result.append('YES')
	else:
		result.append('NO')

for i in result:
	print(i)