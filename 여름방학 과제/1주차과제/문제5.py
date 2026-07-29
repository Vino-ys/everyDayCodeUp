n, k = map(int, input().split())
arr = list(map(int, input().split()))
count = 0

for i in arr:
	if k == 0:
		count += 1
	else:
		if i % k == 0:
			count += 1

print(count)