point = 0
sumPointList = []
n = int(input())
list = list(map(int, input().split()))

for i in range(n):
	point += list[i]
	sumPointList.append(point)

for i in sumPointList:
	print(i, end = " ")