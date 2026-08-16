n = int(input())
num = list(map(int, input().split()))
count = 0
past = 0
max = 0

for i in num:
	if i > past:
		count += 1
		past = i
	else:
		if count > max:
			max = count
		past = i
		count = 1
if count > max:
	max = count

print(max)