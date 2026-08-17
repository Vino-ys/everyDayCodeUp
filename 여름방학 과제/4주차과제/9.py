str = input()
n = int(input())
result = []

for i in range(n):
	s = input()
	for idx, value in enumerate(str):
		if s == value:
			result.append(int(idx) + 1)
			break
		if int(idx) + 1 == len(str):
			result.append('-1')

for i in result:
	print(i)