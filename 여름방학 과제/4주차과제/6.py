n, q = map(int, input().split())
arr = list(map(int, input().split()))

result = []
sumList = [0] * (n + 1)

for i in range(n):
	sumList[i + 1] = sumList[i] + arr[i]

for i in range(q):
	first, end = map(int, input().split())
	result.append(sumList[end] - sumList[first - 1])

for i in result:
	print(i)