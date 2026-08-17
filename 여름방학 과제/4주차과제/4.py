sum = 0
result = []

n = int(input())
num = list(map(int, input().split()))

for i in range(n):
	sum += num[i]
	if i == 0:
		sum += num[i + 1]
	elif i == n - 1:
		sum += num[i - 1]
	else:
		sum += num[i + 1]
		sum += num[i - 1]
	result.append(sum)
	sum = 0

for i in result:
	print(i, end = " ")