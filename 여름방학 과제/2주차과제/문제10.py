n = int(input())
part = []

for i in range(n):
	na, mo, da = input().split()
	part.append((int(mo), int(da), na))

part.sort()

for i in part:
	print(i[2], end = " ")