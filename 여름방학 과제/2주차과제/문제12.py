r, c = map(int, input().split())
arr = []
sum = 0
result = []

for i in range(r):
	raw = list(map(int, input().split()))
	arr.append(raw)

for i in range(c):
	for j in range(r):
		sum += arr[j][i]
	result.append(sum)
	sum = 0

for i in range(c):
	print(result[i], end = " ")