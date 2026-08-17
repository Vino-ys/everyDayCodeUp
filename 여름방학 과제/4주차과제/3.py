sum = 0

r, c = map(int, input().split())
num = []

for i in range(r):
	cList = list(map(int, input().split()))
	num.append(cList)

if r == 1:
	for j in range(c):
		sum += num[0][j]
elif c == 1:
	for j in range(r):
		sum += num[j][0]
else:
	for j in range(c):
		sum += num[0][j]
		sum += num[r - 1][j]
	for j in range(r):
		if j == 0 or j == r - 1:
			continue
		else:
			sum += num[j][0]
			sum += num[j][c - 1]

print(sum)