n = int(input())
numArr = []
max = 0
result = []

for i in range(n):
	num = int(input())
	if num == 0:
		if len(numArr) == 0:
			result.append('-1')
		else:
			for idx, value in enumerate(numArr):
				if value > max:
					max = value
					idxx = idx
			result.append(numArr.pop(idxx))
			max = 0
	else:
		numArr.append(num)

for i in result:
	print(i)