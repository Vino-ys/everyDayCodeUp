count = 0
result = []

n = int(input())
nList = list(map(int, input().split()))
q = int(input())
qList = list(map(int, input().split()))

for i in qList:
	question = i
	for j in range(n):
		if nList[j] == question:
			count += 1
	result.append(count)
	count = 0

for i in result:
	print(i, end = " ")