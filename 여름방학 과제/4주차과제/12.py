n = int(input())
numArr = []
result = []

for i in range(n):
	num = int(input())
	if num == 0:
		if len(numArr) == 0:
			result.append('-1')
		else:
			maxValue = max(numArr)
			maxIdx = numArr.index(maxValue)
			result.append(numArr.pop(maxIdx))
	else:
		numArr.append(num)

for i in result:
	print(i)