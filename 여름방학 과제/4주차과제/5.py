maxNum = 0
result = []

n = int(input())
numList = list(map(int, input().split()))

for i in numList:
	if i > maxNum:
		maxNum = i
	result.append(maxNum)

for i in result:
	print(i, end = " ")