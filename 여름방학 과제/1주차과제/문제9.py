str = input()
re = input()
count = 0

for i in range(len(str)):
	if str[i] == re:
		count += 1

print(count)