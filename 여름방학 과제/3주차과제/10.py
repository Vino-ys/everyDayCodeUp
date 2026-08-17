n = int(input())
list = list(map(int, input().split()))
pay = 0

for i in range(n):
	if list[i] != 0:
		pay += list[i]
	else:
		pay -= list[i - 1]

print(pay)