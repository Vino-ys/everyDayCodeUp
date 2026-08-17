n, k = map(int, input().split())
nlist = list(map(int, input().split()))
nextList = []

for i in range(k):
	nextList.append(nlist.pop())
	for j in nlist:
		nextList.append(j)
	nlist = nextList
	nextList = []

for i in nlist:
	print(i, end = " ")