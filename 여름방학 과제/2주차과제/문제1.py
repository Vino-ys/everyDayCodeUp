Num = int(input())
id = 'a'
list = []
count = 0

for i in range(Num):
	id = input()
	if id not in list:
		list.append(id)

for i in list: count += 1

print(count)
for i in list:
	print(i, end = " ")