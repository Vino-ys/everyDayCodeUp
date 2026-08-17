n, q = map(int, input().split())
list = list(map(int, input().split()))
result = []

for i in range(q):
	first, end = map(int, input().split())
	result.append(sum(list[first - 1:end]))

for i in result:
	print(i)