r, c = map(int, input().split())
result = []
sum = 0

for i in range(r):
	raw = list(map(int, input().split()))
	for j in raw:
		sum += j
	result.append(sum)
	sum = 0

for i in range(r):
	print(result[i], end = " ")