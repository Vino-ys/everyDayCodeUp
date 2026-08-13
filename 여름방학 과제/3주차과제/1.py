r, c = map(int, input().split())
arr = []
reverseArr = []

for i in range(r):
	raw = list(map(int, input().split()))
	arr.append(raw)

for i in range(c):
	exarr = []
	for j in range(r):
		exarr.append(arr[j][i])
	reverseArr.append(exarr)
	
for i in range(c):
	for j in range(r):
		print(reverseArr[i][j], end = " ")
	print()